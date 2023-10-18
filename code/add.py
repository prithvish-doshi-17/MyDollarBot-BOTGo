import helper
import logging
import telebot
import calendar
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from telebot import types
from datetime import datetime

option = {}
exchange_rates = {
    'USD': 1.0,
    'Euro': 0.86,  # Replace with the actual exchange rates
    'INR': 74.22,   # Replace with the actual exchange rates
   }


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

def post_category_selection(message, bot):
    try:
        chat_id = message.chat.id
        selected_category = message.text
        if selected_category not in helper.getSpendCategories():
            bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
            raise Exception("Sorry I don't recognise this category \"{}\"!".format(selected_category))

        option[chat_id] = selected_category
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.row_width = 2
        for c in helper.getCurrencyValues():
        	markup.add(c)
        msg = bot.reply_to(message, 'Which Currency', reply_markup=markup)
        bot.register_next_step_handler(msg, post_currency_input, bot, selected_category)
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

def post_currency_input(message,bot,selected_category):
    try:
        chat_id = message.chat.id
        choice = message.text
        if choice not in helper.getCurrencyValues():
            bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
            raise Exception("Sorry I don't recognise this currency \"{}\"!".format(option))
        converted_currency =''
        
        if choice == "Euro":
            converted_currency = 'Euro'
        elif choice == "INR":
            converted_currency = 'INR'
        elif choice == "USD":
             converted_currency = 'USD'
        else:
            raise Exception("Invalid choice. Please select 1, 2, or 3 for Euro, INR, or GBP, respectively.")
        message = bot.send_message(chat_id, 'How much did you spend on {}? \n(Enter numeric values only)'.format(str(option[chat_id])))
        bot.register_next_step_handler(message, post_amount_input, bot, selected_category, converted_currency)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no. ' + str(e))


def post_amount_input(message, bot, selected_category, converted_currency):
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
                post_date_input(message,result,bot,selected_category,converted_currency,amount_value)
                bot.edit_message_text(
                    f"Selected date: {result}",
                    c.message.chat.id,
                    c.message.message_id,
                )
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no. ' + str(e))

def post_date_input(message, date_entered, bot, selected_category, converted_currency, amount_value):
    try:
        chat_id = message.chat.id
        converted_amount = convert_usd_to(converted_currency, amount_value)
        if converted_amount is not None:
            date_of_entry = helper.validate_entered_date(date_entered)
            date_str, category_str, amount_str, converted_currency_str, converted_amount_str = str(date_of_entry), str(option[chat_id]), str(amount_value), str(converted_currency), str(converted_amount)
            helper.write_json(add_user_record(chat_id, "{},{},{},{},{}".format(date_str, category_str, converted_amount_str, converted_currency_str, amount_str)))
            bot.send_message(chat_id, 'The following expenditure has been recorded: You have spent ${} for {} on {}.\nConverted from {}: {}'.format(converted_amount_str, category_str, date_str, converted_currency_str, amount_str))
            helper.display_remaining_budget(message, bot, selected_category)
        else:
            raise Exception("Invalid currency choice.")
        helper.display_remaining_budget(message, bot, selected_category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(date_entered, 'Oh no. ' + str(e))

def add_user_record(chat_id, record_to_be_added):
    user_list = helper.read_json()
    if str(chat_id) not in user_list:
        user_list[str(chat_id)] = helper.createNewUserRecord()

    user_list[str(chat_id)]['data'].append(record_to_be_added)
    return user_list
def convert_usd_to(currency, amount):
    if currency in exchange_rates:
        converted_amount = float(amount) * exchange_rates[currency]
        return converted_amount
    else:
        return None

