import time
import os
import helper
import graphing
import logging
from telebot import types
from datetime import datetime


def run(message, bot):
    helper.read_json()
    chat_id = message.chat.id
    history = helper.getUserHistory(chat_id)
    if history is None:
        bot.send_message(chat_id, "Sorry, there are no records of the spending!")
    else:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.row_width = 2
        for mode in helper.getSpendDisplayOptions():
            markup.add(mode)
        # markup.add('Day', 'Month')
        msg = bot.reply_to(message, 'Please select a category to see details', reply_markup=markup)
        bot.register_next_step_handler(msg, display_total, bot)

total=""
bud=""
def display_total(message, bot):
    global total
    global bud
    try:
        chat_id = message.chat.id
        DayWeekMonth = message.text

        if DayWeekMonth not in helper.getSpendDisplayOptions():
            raise Exception("Sorry I can't show spendings for \"{}\"!".format(DayWeekMonth))

        history = helper.getUserHistory(chat_id)
        if history is None:
            raise Exception("Oops! Looks like you do not have any spending records!")

        bot.send_message(chat_id, "Hold on! Calculating...")
        # show the bot "typing" (max. 5 secs)
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(0.5)
        total_text = ""
        # get budget data
        budgetData = {}
        if helper.isOverallBudgetAvailable(chat_id):
            budgetData = helper.getOverallBudget(chat_id)
        elif helper.isCategoryBudgetAvailable(chat_id):
            budgetData = helper.getCategoryBudget(chat_id)

        if DayWeekMonth == 'Day':
            query = datetime.now().today().strftime(helper.getDateFormat())
            # query all that contains today's date
            queryResult = [value for index, value in enumerate(history) if str(query) in value]
        elif DayWeekMonth == 'Month':
            query = datetime.now().today().strftime(helper.getMonthFormat())
            # query all that contains today's date
            queryResult = [value for index, value in enumerate(history) if str(query) in value]

        total_text = calculate_spendings(queryResult)
        total=total_text
        bud=budgetData
        spending_text = display_budget_by_text(history, budgetData)
        if len(total_text) == 0:
            spending_text += "----------------------\nYou have no spendings for {}!".format(DayWeekMonth)
            bot.send_message(chat_id, spending_text)
        else:
            spending_text += "\n----------------------\nHere are your total spendings {}:\nCATEGORIES,AMOUNT \n----------------------\n{}".format(
                DayWeekMonth.lower(), total_text)
            bot.send_message(chat_id, spending_text)
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.row_width = 2
            for plot in helper.getplot():
               markup.add(plot)
              # markup.add('Day', 'Month')
            msg = bot.reply_to(message, 'Please select a plot to see the total expense', reply_markup=markup)
            bot.register_next_step_handler(msg, plot_total, bot)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, str(e))

def plot_total(message, bot):
     chat_id = message.chat.id
     pyi=message.text
     if pyi == 'Bar with budget':
       
       graphing.visualize(total,bud)
       bot.send_photo(chat_id, photo=open('expenditure.png', 'rb'))
       os.remove('expenditure.png')
     elif pyi == 'Bar without budget': 
       graphing.viz(total)
       bot.send_photo(chat_id, photo=open('expend.png', 'rb'))
       os.remove('expend.png')
     else:
       graphing.vis(total)
       bot.send_photo(chat_id, photo=open('pie.png', 'rb'))
       os.remove('pie.png')
def calculate_spendings(queryResult):
    total_dict = {}

    for row in queryResult:
        # date,cat,money
        s = row.split(',')
        # cat
        cat = s[1]
        if cat in total_dict:
            # round up to 2 decimal
            total_dict[cat] = round(total_dict[cat] + float(s[2]), 2)
        else:
            total_dict[cat] = float(s[2])
    total_text = ""
    for key, value in total_dict.items():
        total_text += str(key) + " $" + str(value) + "\n"
    return total_text


def display_budget_by_text(history, budget_data) -> str:
    query = datetime.now().today().strftime(helper.getMonthFormat())
    # query all expense history that contains today's date
    queryResult = [value for index, value in enumerate(history) if str(query) in value]
    total_text = calculate_spendings(queryResult)
    budget_display = ""
    total_text_split = [line for line in total_text.split('\n') if line.strip() != '']

    if isinstance(budget_data, str):
        # if budget is string denoting it is overall budget
        budget_val = float(budget_data)
        total_expense = 0
        # sum all expense
        for expense in total_text_split:
            a = expense.split(' ')
            amount = a[1].replace("$", "")
            total_expense += float(amount)
        # calculate the remaining budget
        remaining = budget_val - total_expense
        # set the return message
        budget_display += "Overall Budget is: " + str(budget_val) + "\n----------------------\nCurrent remaining budget is " + str(
            remaining) + "\n"
    elif isinstance(budget_data, dict):
        budget_display += "Budget by Catergories is:\n"
        categ_remaining = {}
        # categorize the budgets by their categories
        for key in budget_data.keys():
            budget_display += key + ":" + budget_data[key] + "\n"
            categ_remaining[key] = float(budget_data[key])
        #  calculate the remaining budgets by categories
        for i in total_text_split:
            # the expense text is in the format like "Food $100"
            a = i.split(' ')
            a[1] = a[1].replace("$", "")
            categ_remaining[a[0]] = categ_remaining[a[0]] - float(a[1]) if a[0] in categ_remaining else -float(a[1])
        budget_display += "----------------------\nCurrent remaining budget is: \n"
        # show the remaining budgets
        for key in categ_remaining.keys():
            budget_display += key + ":" + str(categ_remaining[key]) + "\n"
    return budget_display
