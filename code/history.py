import helper
import logging
import matplotlib.pyplot as plt
from datetime import datetime
from telebot import types

def run(message, bot):
    try:
        helper.read_json()
        chat_id = message.chat.id
        user_income_history = helper.getUserIncomeHistory(chat_id)
        user_expense_history = helper.getUserExpenseHistory(chat_id)
        spend_total_str = ""
        income_total_str = ""
        # Amount for each month
        income_amount=0.0
        expense_amount=0.0
        am=""
        Dict_income = {'Jan': 0.0,'Feb': 0.0,'Mar': 0.0,'Apr': 0.0,'May': 0.0, 'Jun': 0.0, 'Jul': 0.0, 'Sep': 0.0, 'Oct': 0.0, 'Nov': 0.0, 'Dec': 0.0}
        Dict_expense = {'Jan': 0.0,'Feb': 0.0,'Mar': 0.0,'Apr': 0.0,'May': 0.0, 'Jun': 0.0, 'Jul': 0.0, 'Sep': 0.0, 'Oct': 0.0, 'Nov': 0.0, 'Dec': 0.0}
        Dict_profit = {'Jan': 0.0,'Feb': 0.0,'Mar': 0.0,'Apr': 0.0,'May': 0.0, 'Jun': 0.0, 'Jul': 0.0, 'Sep': 0.0, 'Oct': 0.0, 'Nov': 0.0, 'Dec': 0.0}
        if user_income_history and user_expense_history is None:
            raise Exception("Sorry! No records found!")
        spend_total_str = "Here is your spending history : \nDATE, CATEGORY, AMOUNT\n----------------------\n"
        if len(user_expense_history) == 0:
            spend_total_str = "Sorry! No spending records found!"
        else:
            for rec in user_expense_history:
                spend_total_str += str(rec) + "\n"
                av=str(rec).split(",")
                ax=av[0].split("-")
                am=ax[1]
                expense_amount=Dict_expense[am]+ float(av[2])
                Dict_expense[am]=expense_amount
                Dict_expense[am]= 0.0 - Dict_expense[am]
                Dict_profit[am] = Dict_profit[am] + Dict_expense[am]
        bot.send_message(chat_id, spend_total_str)

        income_total_str = "Here is your income history : \nDATE, CATEGORY, AMOUNT\n----------------------\n"
        if len(user_income_history) == 0:
            income_total_str = "Sorry! No income records found!"
        else:
            for rec in user_income_history:
                income_total_str += str(rec) + "\n"
                av=str(rec).split(",")
                ax=av[0].split("-")
                am=ax[1]
                income_amount=Dict_income[am]+ float(av[2])
                Dict_income[am] = income_amount
                Dict_profit[am] = Dict_profit[am] + Dict_income[am]
        bot.send_message(chat_id, income_total_str)
       
        selected_duration = ""
        category_expenses = {}
        duration_expenses = {}
        
        for record in user_expense_history:
            date, category, amount = record.split(",")
            date_obj = datetime.strptime(date, "%d-%b-%Y %H:%M")
            
            # Calculate expenses for the selected duration
            if selected_duration == "Day":
                duration_key = date_obj.strftime("%d-%b-%Y")
            elif selected_duration == "Week":
                duration_key = date_obj.strftime("%Y-%U")
            elif selected_duration == "Month":
                duration_key = date_obj.strftime("%Y-%b")

            if duration_key in duration_expenses:
                duration_expenses[duration_key] += float(amount)
            else:
                duration_expenses[duration_key] = float(amount)
            
            # Calculate category-wise expenses
            if category in category_expenses:
                category_expenses[category] += float(amount)
            else:
                category_expenses[category] = float(amount)
        
        # Sort category-wise and duration-wise expenses in descending order
        sorted_category_expenses = sorted(category_expenses.items(), key=lambda x: x[1], reverse=True)
        sorted_duration_expenses = sorted(duration_expenses.items(), key=lambda x: x[1], reverse=True)
        
        # Prepare and send the summary messages
        bot.send_message(chat_id, f"Summary of Expenses ({selected_duration}-wise) in Descending Order:\n")
        
        # Display category-wise expenses
        bot.send_message(chat_id, "Category-Wise Expenses:")
        for category, total in sorted_category_expenses:
            bot.send_message(chat_id, f"{category}: ${total:.2f}")

        # Display duration-wise expenses
        bot.send_message(chat_id, f"{selected_duration}-Wise Expenses:")
        for duration, total in sorted_duration_expenses:
            bot.send_message(chat_id, f"{duration}: ${total:.2f}")
        
       # bot.send_message(chat_id, Dict[am])
        plt.clf()
        width=1.0
        x = Dict_income.keys()
        y1 = Dict_income.values()
        y2 = Dict_expense.values()
        y3 = Dict_profit.values()
        plt.bar(x, y1, width, color='g')
        # plt.savefig('histo_income.png')
        # bot.send_photo(chat_id, photo=open('histo_income.png','rb'))

        # plt.clf()
        # width=1.0
        plt.bar(x, y2, width, color='r')
        plt.plot(x, y3, label='Line', color='blue', marker='o')
        plt.grid(True)
        plt.savefig('histo_expense.png')
        bot.send_photo(chat_id, photo=open('histo_expense.png','rb'))
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        options = {"Yes", "No"}
        markup.row_width = 2
        for c in options.values():
            markup.add(c)
        msg = bot.reply_to(message, 'Do you want to see detailed history of income or expenses', reply_markup=markup)
        bot.register_next_step_handler(msg, post_detailed_history, bot)
        ##bot.send_message(chat_id, amount)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "No records exist" )

def post_detailed_history(message, bot):
    try:
        chat_id = message.chat.id
        selected = message.text
        if selected == "Yes":
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            options = helper.getIncomeOrExpense()
            markup.row_width = 2
            for c in options.values():
                markup.add(c)
            msg = bot.reply_to(message, 'Select Income or Expense', reply_markup=markup)
            bot.register_next_step_handler(msg, post_type_selection, bot)
        else:
            bot.send_message(chat_id, "Please type /menu to go back.")
    except Exception as e:
        # print("hit exception")
        helper.throw_exception(e, message, bot, logging)

def post_type_selection(message, bot):
    try:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        chat_id = message.chat.id
        selectedType = message.text
        selected_duration = ""
        category_expenses = {}
        duration_expenses = {}
        user_history = helper.getUserHistory(chat_id, selectedType)
        for record in user_history:
            date, category, amount = record.split(",")
            date_obj = datetime.strptime(date, "%d-%b-%Y %H:%M")
            
            # Calculate expenses for the selected duration
            if selected_duration == "Day":
                duration_key = date_obj.strftime("%d-%b-%Y")
            elif selected_duration == "Week":
                duration_key = date_obj.strftime("%Y-%U")
            elif selected_duration == "Month":
                duration_key = date_obj.strftime("%Y-%b")

            if duration_key in duration_expenses:
                duration_expenses[duration_key] += float(amount)
            else:
                duration_expenses[duration_key] = float(amount)
            
            # Calculate category-wise expenses
            if category in category_expenses:
                category_expenses[category] += float(amount)
            else:
                category_expenses[category] = float(amount)
        
        # Sort category-wise and duration-wise expenses in descending order
        sorted_category_expenses = sorted(category_expenses.items(), key=lambda x: x[1], reverse=True)
        sorted_duration_expenses = sorted(duration_expenses.items(), key=lambda x: x[1], reverse=True)
        
        # Prepare and send the summary messages
        bot.send_message(chat_id, f"Summary of Expenses ({selected_duration}-wise) in Descending Order:\n")
        
        # Display category-wise expenses
        bot.send_message(chat_id, "Category-Wise Expenses:")
        for category, total in sorted_category_expenses:
            bot.send_message(chat_id, f"{category}: ${total:.2f}")

        # Display duration-wise expenses
        bot.send_message(chat_id, f"{selected_duration}-Wise Expenses:")
        for duration, total in sorted_duration_expenses:
            bot.send_message(chat_id, f"{duration}: ${total:.2f}")

    except Exception as e:
        # print("hit exception")
        helper.throw_exception(e, message, bot, logging)