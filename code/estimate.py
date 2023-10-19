import time
import helper
import logging
from telebot import types


def run(message, bot):
    helper.read_json()
    chat_id = message.chat.id
    history = helper.getUserExpenseHistory(chat_id)
    if history is None:
        bot.send_message(
            chat_id, "Oops! Looks like you do not have any spending records!")
    else:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.row_width = 2
        for mode in helper.getSpendEstimateOptions():
            markup.add(mode)
        # markup.add('Day', 'Month')
        msg = bot.reply_to(
            message, 'Please select the period to estimate',
            reply_markup=markup)
        bot.register_next_step_handler(msg, estimate_total, bot)


def estimate_total(message, bot):
    try:
        chat_id = message.chat.id
        DayWeekMonth = message.text

        if DayWeekMonth not in helper.getSpendEstimateOptions():
            raise Exception(
                "Sorry I can't show an estimate for \"{}\"!".format(
                    DayWeekMonth))

        history = helper.getUserHistory(chat_id)
        if history is None:
            raise Exception(
                "Oops! Looks like you do not have any spending records!")

        bot.send_message(chat_id, "Hold on! Calculating...")
        # show the bot "typing" (max. 5 secs)
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(0.5)

        total_text = ""
        days_to_estimate = 0
        if DayWeekMonth == 'Next day':
            days_to_estimate = 1
        elif DayWeekMonth == 'Next month':
            days_to_estimate = 30
            # query all that contains today's date
        # query all that contains all history
        queryResult = [value for index, value in enumerate(history)]

        total_text = calculate_estimate(queryResult, days_to_estimate)

        spending_text = ""
        if len(total_text) == 0:
            spending_text = "You have no estimate for {}!".format(DayWeekMonth)
        else:
            spending_text = "Here are your estimated spendings"
            spending_text += " for the " + DayWeekMonth.lower()
            spending_text += ":\nCATEGORIES,AMOUNT \n----------------------\n"
            spending_text += total_text

        bot.send_message(chat_id, spending_text)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, str(e))


def calculate_estimate(queryResult, days_to_estimate):
    total_dict = {}
    days_data_available = {}
    for row in queryResult:
        # date,cat,money
        s = row.split(',')
        # cat
        cat = s[1]
        date_str = s[0][0:11]
        if cat in total_dict:
            # round up to 2 decimal
            total_dict[cat] = round(total_dict[cat] + float(s[2]), 2)
        else:
            total_dict[cat] = float(s[2])
        if date_str not in days_data_available:
            days_data_available[date_str] = True

    total_text = ""
    for key, value in total_dict.items():
        category_count = len(days_data_available)
        daily_avg = value / category_count
        estimated_avg = round(daily_avg * days_to_estimate, 2)
        total_text += str(key) + " $" + str(estimated_avg) + "\n"
    return total_text
