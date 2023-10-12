import helper
import logging
from telebot import types
from datetime import datetime


option = {}


def run(message, bot):
    helper.read_json()
    chat_id = message.chat.id
    option.pop(chat_id, None)  # remove temp choice
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    for c in helper.getIncomeCategories():
        markup.add(c)
    msg = bot.reply_to(message, 'Select Category', reply_markup=markup)
    bot.register_next_step_handler(msg, post_category_selection, bot)


def post_category_selection(message, bot):
    try:
        chat_id = message.chat.id
        selected_category = message.text
        if selected_category not in helper.getIncomeCategories():
            bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
            raise Exception("Sorry I don't recognise this category \"{}\"!".format(selected_category))

        option[chat_id] = selected_category
        message = bot.send_message(chat_id, 'How much did you receive through {}? \n(Enter numeric values only)'.format(str(option[chat_id])))
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
            raise Exception("Income amount has to be a non-zero number.")

        date_of_entry = datetime.today().strftime(helper.getDateFormat() + ' ' + helper.getTimeFormat())
        date_str, income_category_str, income_amount_str = str(date_of_entry), str(option[chat_id]), str(amount_value)
        helper.write_json(add_user_record(chat_id, "{},{},{}".format(date_str, income_category_str, income_amount_str)))
        bot.send_message(chat_id, 'The following income has been recorded: You have recieved ${} for {} on {}'.format(income_amount_str, income_category_str, date_str))
        # helper.display_remaining_budget(message, bot, selected_category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no. ' + str(e))


def add_user_record(chat_id, record_to_be_added):
    user_list = helper.read_json()
    if str(chat_id) not in user_list:
        user_list[str(chat_id)] = helper.createNewUserRecord()

    user_list[str(chat_id)]['income_data'].append(record_to_be_added)
    return user_list
