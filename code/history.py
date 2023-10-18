import helper
import logging
import matplotlib.pyplot as plt
from datetime import datetime
def run(message, bot):
    try:
        helper.read_json()
        chat_id = message.chat.id
        user_history = helper.getUserHistory(chat_id)
        spend_total_str = ""
        # Amount for each month
        amount=0.0
        am=""
        Dict = {'Jan': 0.0,'Feb': 0.0,'Mar': 0.0,'Apr': 0.0,'May': 0.0, 'Jun': 0.0, 'Jul': 0.0, 'Sep': 0.0, 'Oct': 0.0, 'Nov': 0.0, 'Dec': 0.0}
        if user_history is None:
            raise Exception("Sorry! No spending records found!")
        spend_total_str = "Here is your spending history : \nDATE, CATEGORY, AMOUNT\n----------------------\n"
        if len(user_history) == 0:
            spend_total_str = "Sorry! No spending records found!"
        else:
            for rec in user_history:
                spend_total_str += str(rec) + "\n"
                av=str(rec).split(",")
                ax=av[0].split("-")
                am=ax[1]
                amount=Dict[am]+ float(av[2])
                Dict[am]=amount
        bot.send_message(chat_id, spend_total_str)
        selected_duration = "Month"

        # Collect and process data
        category_expenses = {}
        duration_expenses = {}
        
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
        
       ## bot.send_message(chat_id, Dict[am])
        plt.clf()
        width=1.0
        plt.bar(Dict.keys(), Dict.values(), width, color='g')
        plt.savefig('histo.png')
        bot.send_photo(chat_id, photo=open('histo.png','rb'))
        ##bot.send_message(chat_id, amount)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops!" + str(e))
