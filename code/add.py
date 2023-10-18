import helper
import logging
import telebot
import calendar
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from telebot import types
from datetime import datetime

option = {}


def run(message, bot):
    helper.read_json()
    chat_id = message.chat.id
    option.pop(chat_id, None)  # remove temp choice
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    for c in helper.getSpendCategories():
        markup.add(c)
    msg = bot.reply_to(message, 'Select Category', reply_markup=markup)
    bot.register_next_step_handler(msg, post_category_selection, bot)
   
def create_calendar(year=None,month=None):
    now = datetime.datetime.now()
    if year == None: year = now.year
    if month == None: month = now.month
    data_ignore = create_callback_data("IGNORE", year, month, 0)
    keyboard = []
    #First row - Month and Year
    row=[]
    row.append(InlineKeyboardButton(calendar.month_name[month]+" "+str(year),callback_data=data_ignore))
    keyboard.append(row)
    #Second row - Week Days
    row=[]
    for day in ["Mo","Tu","We","Th","Fr","Sa","Su"]:
        row.append(InlineKeyboardButton(day,callback_data=data_ignore))
    keyboard.append(row)

    my_calendar = calendar.monthcalendar(year, month)
    for week in my_calendar:
        row=[]
        for day in week:
            if(day==0):
                row.append(InlineKeyboardButton(" ",callback_data=data_ignore))
            else:
                row.append(InlineKeyboardButton(str(day),callback_data=create_callback_data("DAY",year,month,day)))
        keyboard.append(row)
    #Last row - Buttons
    row=[]
    row.append(InlineKeyboardButton("<",callback_data=create_callback_data("PREV-MONTH",year,month,day)))
    row.append(InlineKeyboardButton(" ",callback_data=data_ignore))
    row.append(InlineKeyboardButton(">",callback_data=create_callback_data("NEXT-MONTH",year,month,day)))
    keyboard.append(row)

    return InlineKeyboardMarkup(keyboard)
    
def send_calendar(message, bot):
    print(bot)
    chat_id=message.chat.id
    message_text = "Please select a date from the calendar below:"
    bot.send_message(chat_id, message_text, reply_markup=create_calendar())
    
def post_category_selection(message, bot):
    try:
        chat_id = message.chat.id
        selected_category = message.text
        if selected_category not in helper.getSpendCategories():
            bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
            raise Exception("Sorry I don't recognise this category \"{}\"!".format(selected_category))

        option[chat_id] = selected_category
        message = bot.send_message(chat_id, 'How much did you spend on {}? \n(Enter numeric values only)'.format(str(option[chat_id])))
        bot.register_next_step_handler(message, post_amount_input, bot, selected_category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no! ' + str(e))
        display_text = ""
        commands = helper.getCommands()
        for c in commands:  # generate help text out of the commands dictionary defined at the top
            display_text += "/" + c + ": "
            display_text += commands[c] + "\n"
        bot.send_message(chat_id, 'Please select a menu option from below:')
        bot.send_message(chat_id, display_text)


def post_amount_input(message, bot, selected_category):
    try:
        chat_id = message.chat.id
        amount_entered = message.text
        amount_value = helper.validate_entered_amount(amount_entered)  # validate
        if amount_value == 0:  # cannot be $0 spending
            raise Exception("Spent amount has to be a non-zero number.")
            
        date=datetime.today()
        calendar, step = DetailedTelegramCalendar().build()
        bot.send_message(chat_id, f"Select {LSTEP[step]}", reply_markup=calendar)

        @bot.callback_query_handler(func=DetailedTelegramCalendar.func())
        def cal(c):
            result, key, step = DetailedTelegramCalendar().process(c.data)

            if not result and key:
                bot.edit_message_text(
                    f"Select {LSTEP[step]}",
                    c.message.chat.id,
                    c.message.message_id,
                    reply_markup=key,
                )
            elif result:
                post_date_input(message,result,bot,selected_category,amount_value)
                bot.edit_message_text(
                    f"Selected date: {result}",
                    c.message.chat.id,
                    c.message.message_id,
                )
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no. ' + str(e))

def post_date_input(message, date, bot, selected_category, amount_value):
    try:
        chat_id = message.chat.id
        date_entered = date
        date_of_entry = helper.validate_entered_date(date_entered)  # validate
        date_str, category_str, amount_str = str(date_of_entry), str(option[chat_id]), str(amount_value)
        helper.write_json(add_user_record(chat_id, "{},{},{}".format(date_str, category_str, amount_str)))
        bot.send_message(chat_id, 'The following expenditure has been recorded: You have spent ${} for {} on {}'.format(amount_str, category_str, date_str))
        helper.display_remaining_budget(message, bot, selected_category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(date, 'Oh no. ' + str(e))

def add_user_record(chat_id, record_to_be_added):
    user_list = helper.read_json()
    if str(chat_id) not in user_list:
        user_list[str(chat_id)] = helper.createNewUserRecord()

    user_list[str(chat_id)]['data'].append(record_to_be_added)
    return user_list
