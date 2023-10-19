# About MyExpense's /add Feature
This feature enables the user to add a new income or expense to their income or expense tracker.

Currently we have the following expense categories set by default:

- Food
- Groceries
- Utilities
- Transport
- Shopping
- Miscellaneous

Currently we have the following income categories set by default:

- Work
- Volunteering
- Part-Time
- Prizes
- Miscellaneous

The user can choose a category from income or expense set and add the amount they have spent or received to be stored in the income and expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/nainisha-b/MyExpenseBot/blob/main/code/add.py)

# Code Description
## Functions

1. run(message, bot):
 This is the main function used to implement the add feature. It requests the user to choose their income or expense category, after which control is given to post_type_selection(message, bot) for further processing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. post_type_selection(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the add.py file. It pop ups a menu to choose the type in between income and expense. After selecting the type of input, It pop ups a menu on the bot asking the user to choose their income or expense category, after which control is given to post_category_selection(message, bot, selectedType) for further processing. 

3. post_category_selection(message, bot, selectedType):
 It takes 3 arguments for processing - **message** which is the message from the user, **bot** which is the telegram bot object, **selectedType** which is the type selected in between income and expense from the post_type_selection(message, bot): function in the add.py file. It stores the category selected from post_type_selection(message, bot) and requests the user to select the type of currency from the menu and then passes control to post_currency_input(message, bot, selectedType, selected_category) for further processing.

4. post_currency_input(message,bot,selectedType, selected_category):
 It takes 4 arguments for processing - **message** which is the message from the user, **bot** which is the telegram bot object, **selectedType** which is the type selected in between income and expense and **selected_category** which is the category selected by user in income or expense categories from the post_category_selection(message, bot, selectedType): function in the add.py. It stores the type of currency and requests the user to enter the amount they have spent on the income or expense category chosen and then passes control to post_amount_input(message, bot, selectedType, selected_category, converted_currency) for further processing.

5. post_amount_input(message, bot, selectedType, selected_category, converted_currency):
 It takes 5 arguments for processing - **message** which is the message from the user, **bot** which is the telegram bot, **selectedType** which is the type selected in between income and expense, **selected_category** which is the category selected by user in income or expense categories object and **converted_currency** which is the type of currency selected by the user from the post_currency_input(message,bot,selectedType, selected_category): function in the add.py file. It takes the amount entered by the user and validates it with helper.validate_entered_amount() and pop ups a calendar for user to take income or expense date input from the user and then passes control to post_date_input(message, date_entered, bot, selectedType, selected_category, converted_currency, amount_value) for further processing.

 6. post_date_input(message, date_entered, bot, selectedType, selected_category, converted_currency, amount_value):
 It takes 6 arguments for processing - **message** which is the message from the user, **bot** which is the telegram bot, **selectedType** which is the type selected in between income and expense, **selected_category** which is the category selected by user in income or expense categories object, **converted_currency** which is the type of currency selected by the user and **amount_value** which is the amount entered by the user from the post_amount_input(message, bot, selectedType, selected_category, converted_currency): function in the add.py file. It takes the date selected by the user using calendar and validated it with helper.validate_selected_date() and converts the amount input from the input currency type to default type i.e., USD and then calls add_user_income_record or add_user_expense_record based on the selectedType to store the data.

7. add_user_income_record(chat_id, record_to_be_added):
 It takes 2 arguments for processing - **chat_id** which is the chat_id of the user's chat, and **record_to_be_added** which is the income record to be added to the store. It then stores this income record in the store.

8. add_user_expense_record(chat_id, record_to_be_added):
 It takes 2 arguments for processing - **chat_id** which is the chat_id of the user's chat, and **record_to_be_added** which is the expense record to be added to the store. It then stores this expense record in the store.

9. convert_usd_to(currency, amount):
 It takes 2 arguments for processing - **currency** which is the currency type from the user, and **amount** which is the amount value entered by the user. This method is being called in post_date_input(message, date_entered, bot, selectedType, selected_category, converted_currency, amount_value) to convert the custom currency type to default currency type which is USD.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.

Below you can see an example in text format:

ExpenseBot, [10/18/2023 11:56 PM]
Select Income or Expense

Anvitha, [10/18/2023 11:56 PM]
Income

ExpenseBot, [10/18/2023 11:56 PM]
Select Category

Anvitha, [10/18/2023 11:56 PM]
Work

ExpenseBot, [10/18/2023 11:56 PM]
Select Currency

Anvitha, [10/18/2023 11:56 PM]
Euro

ExpenseBot, [10/18/2023 11:56 PM]
How much did you receive through Work? 
(Enter numeric values only)

Anvitha, [10/18/2023 11:56 PM]
60

ExpenseBot, [10/18/2023 11:56 PM]
Date is set: 2022-12-21

ExpenseBot, [10/18/2023 11:56 PM]
The following expenditure has been recorded: You have spent/received $63.0 for Work on 21-Dec-22. Actual currency is Euro and value is 60.0