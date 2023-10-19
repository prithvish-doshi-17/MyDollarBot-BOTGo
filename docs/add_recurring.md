# About MyexpenseBot's /add_recurring Feature
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
This feature enables the user to add a new expense to their expense tracker.


The user can choose a an existing category or add custom category and add the amount they have spent to be stored in the expense tracker.

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


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add_recurring into the telegram bot.

Below you can see an example in text format:

ExpenseBot, [19.10.23 01:18]
[In reply to Vaishnavi]
Select Category

Vaishnavi, [19.10.23 01:19]
Food

ExpenseBot, []
How much did you spend on Food? 
(Enter numeric values only)

Vaishnavi, [19.10.23 01:19]
15

ExpenseBot, [19.10.23 01:20]
For how many months in the future will the expense be there?
(Enter integer values only)

Vaishnavi, [19.10.23 01:20]
6

dollarbot, [19.10.23 01:20]
The following expenditure has been recorded: You have spent $15.0 for Food for the next 6 months
