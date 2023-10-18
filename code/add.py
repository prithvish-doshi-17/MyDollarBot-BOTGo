import helper
import logging
import telebot
import calendar
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from telebot import types
from datetime import datetime

option = {}


def run(message, bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    options = helper.getIncomeOrExpense()
    markup.row_width = 2
    for c in options.values():
        markup.add(c)
    msg = bot.reply_to(message, 'Select Income or Expense', reply_markup=markup)
    bot.register_next_step_handler(msg, post_type_selection, bot)

def post_type_selection(message, bot):
    try:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        chat_id = message.chat.id
        selectedType = message.text
        if selectedType == "Income":
            for c in helper.getIncomeCategories():
                markup.add(c)
        else:
            for c in helper.getSpendCategories():
                markup.add(c)
        msg = bot.reply_to(message, 'Select Category', reply_markup=markup)
        bot.register_next_step_handler(msg, post_category_selection, bot, selectedType)
    except Exception as e:
        # print("hit exception")
        helper.throw_exception(e, message, bot, logging)

def post_category_selection(message, bot, selectedType):
    try:
        chat_id = message.chat.id
        selected_category = message.text
        if selectedType == "Income":
            categories = helper.getIncomeCategories()
        else:
            categories = helper.getSpendCategories()
        if selected_category not in categories:
            bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
            raise Exception("Sorry I don't recognise this category \"{}\"!".format(selected_category))

        option[chat_id] = selected_category
        if selectedType == "Income" :
            message = bot.send_message(chat_id, 'How much did you receive through {}? \n(Enter numeric values only)'.format(str(option[chat_id])))
        else:
            message = bot.send_message(chat_id, 'How much did you spend on {}? \n(Enter numeric values only)'.format(str(option[chat_id])))
        bot.register_next_step_handler(message, post_amount_input, bot, selectedType, selected_category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no. ' + str(e))


def post_amount_input(message, bot, selectedType, selected_category):
    try:
        chat_id = message.chat.id
        amount_entered = message.text
        amount_value = helper.validate_entered_amount(amount_entered)  # validate
        if amount_value == 0:  # cannot be $0 spending
            raise Exception("Spent amount has to be a non-zero number.")
            
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
                post_date_input(message,result,bot, selectedType, selected_category,amount_value)
                bot.edit_message_text(
                    f"Date is set: {result}",
                    c.message.chat.id,
                    c.message.message_id,
                )
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no. ' + str(e))

def post_date_input(message, date_entered, bot, selectedType, selected_category, amount_value):
    try:
        chat_id = message.chat.id

        date_str, category_str, amount_str = str(date_entered), str(option[chat_id]), str(amount_value)
        if selectedType=="Income":
            helper.write_json(add_user_income_record(chat_id, "{},{},{}".format(date_str, category_str, amount_str)))
        else:
            helper.write_json(add_user_expense_record(chat_id, "{},{},{}".format(date_str, category_str, amount_str)))
        bot.send_message(chat_id, 'The following expenditure has been recorded: You have spent/received ${} for {} on {}.\n'.format(amount_str, category_str, date_str))
        helper.display_remaining_budget(message, bot, selected_category)

    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(date_entered, 'Oh no. ' + str(e))

def add_user_expense_record(chat_id, record_to_be_added):
    user_list = helper.read_json()
    if str(chat_id) not in user_list:
        user_list[str(chat_id)] = helper.createNewUserRecord()

    user_list[str(chat_id)]['expense_data'].append(record_to_be_added)
    return user_list

def add_user_income_record(chat_id, record_to_be_added):
    user_list = helper.read_json()
    if str(chat_id) not in user_list:
        user_list[str(chat_id)] = helper.createNewUserRecord()

    user_list[str(chat_id)]['income_data'].append(record_to_be_added)
    return user_list


