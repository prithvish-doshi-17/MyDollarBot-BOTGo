import helper
import logging
import matplotlib.pyplot as plt

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
       
       ## bot.send_message(chat_id, Dict[am])
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
        ##bot.send_message(chat_id, amount)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops!" + str(e))