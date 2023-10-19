# About MyExpenseBot /history Feature
This feature enables the user to view all of their stored records i.e it gives a historical view of all the expenses stored in MyExpenseBot.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/nainisha-b/MyExpenseBot/blob/main/code/history.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the history feature. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. It calls helper.py to get the user's historical data and based on whether there is data available, it either prints an error message or displays the user's historical data.
2. post_detailed_history(message, bot):
In this function, we are asking users choice to store the history data of either of their expenses or income. Here, **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. It calls helper.py to get the user's historical data and based on whether there is data available, it either prints an error message or displays the user's historical data.
3. post_type_selection(message, bot):
In this function we are recording the time at which the expenses were and sorting the expense history category wise and month(duration) wise in descending order. Here, **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. It calls helper.py to get the user's historical data and based on whether there is data available, it either prints an error message or displays the user's historical data.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.

Below you can see an example in text format:

vaishnew1, [10/15/23 3:01 PM]
Here is your spending history : 
DATE, CATEGORY, AMOUNT
----------------------
14-Oct-2023 19:58,Food,20.0
14-Oct-2023 19:58,Utilities,30.0
14-Oct-2023 20:08,Utilities,20.0
14-Oct-2023 20:09,Utilities,30.0
14-Oct-2023 20:25,Utilities,40.0
14-Oct-2023 21:44,Food,10.0
14-Oct-2023 21:44,Groceries,20.0
14-Oct-2023 21:45,Food,30.0

vaishnew1, [10/15/23 3:01 PM]
Summary of Expenses (Month-wise) in Descending Order:

vaishnew1, [10/15/23 3:01 PM]
Category-Wise Expenses:

vaishnew1, [10/15/23 3:01 PM]
Utilities: $120.00

vaishnew1, [10/15/23 3:01 PM]
Food: $60.00

vaishnew1, [10/15/23 3:01 PM]
Groceries: $20.00

vaishnew1, [10/15/23 3:01 PM]
Month-Wise Expenses:

vaishnew1, [10/15/23 3:02 PM]
2023-Oct: $200.00

Along with the spending history, the histogram displaying spending of each month is plotted, which can help user to manage his/her expenses.

![Test Image ](https://github.com/nainisha-b/MyExpenseBot/blob/main/histo.png)
