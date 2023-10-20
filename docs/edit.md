# About MyExpenseBot's /edit Feature
This feature enables the user to edit a previously entered expense in the app. The use can change the amount set in the bot with this command. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/nainisha-b/MyExpenseBot/blob/main/code/edit.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the edit feature. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. It gets the details for the income or expense to be edited from here and passes control onto select_income_or_expense_to_be_edited(message, bot) for further processing.

2. select_income_or_expense_to_be_edited(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the  run(message, bot): function in the same file. It takes the income or expense as in input through pop up menu and displays the income or expense history as a menu so that user can select the details in the history by the option in the menu. then user is asked to select the income or expense which they want to edit, passing control on to select_category_to_be_updated(message, bot, selectedType): for further processing.

3. def select_category_to_be_updated(message, bot, selectedType):
It takes 3 arguments for processing - **message** which is the message from the user, **bot** which is the telegram bot object and **selectedType** which is the type selected in between income and expense from the select_income_or_expense_to_be_edited(message, bot): function in the same file. Based on income or expense chosen for editing by the user, it separates the date, category and amount component and redirects to the enter_updated_data(m, bot, selected_data, selectedType) for further processing.

4. def enter_updated_data(message, bot, selected_data, selectedType):
It takes 4 arguments for processing - **message** which is the message from the user, **bot** which is the telegram bot object, **selectedType** which is the type selected in between income and expense and **selected_data** which is the specific income or expense data from income or expense history from the select_category_to_be_updated(m, bot, selectedType): function in the same file. It requests the user to select which type of data user wishes to update through a pop up menu and based on selection it takes new data which needs to be updated as input and redirects to different edit functions for further processing.

5. def edit_date(message, bot, selected_data, selectedType, result):
It takes 5 arguments for processing - **message** which is the message from the user, **bot** which is the telegram bot object, **selectedType** which is the type selected in between income and expense, **selected_data** which is the specific income or expense data from income or expense history and **result** which is the new date input which replaces the old date given by the user from enter_updated_data(message, bot, selected_data, selectedType): function in the same file. It reads the user history and replaces the date selected by user with result after validating the date using helper.validate_entered_date()function and displays a text to user that updation is successful.

6. def edit_cat(message, bot, selected_data, selectedType):
It takes 4 arguments for processing - **message** which is the message from the user, **bot** which is the telegram bot object, **selectedType** which is the type selected in between income and expense and **selected_data** which is the specific income or expense data from income or expense history from enter_updated_data(message, bot, selected_data, selectedType): function in the same file. It reads the user history and replaces the category selected by user with the desired category given by the user and it displays that the category update is successful.

6. def edit_cost(m, bot, selected_data, selectedType):
It takes 4 arguments for processing - **message** which is the message from the user, **bot** which is the telegram bot object, **selectedType** which is the type selected in between income and expense and **selected_data** which is the specific income or expense data from income or expense history from enter_updated_data(message, bot, selected_data, selectedType): function in the same file. It reads the user history and replaces the income or expense amount selected by user with the desired income or expense given by the user after validating the amount entered by the user using helper.validate_entered_amount() function and it displays that the income or expense amount is updated.

# How to run this feature?

Anvitha, [10/19/2023 8:39 AM]
/edit

MyExpenseBot, [10/19/2023 8:39 AM]
Edit Income or Expense History

Anvitha, [10/19/2023 8:39 AM]
Income

MyExpenseBot, [10/19/2023 8:39 AM]
Select income/expense to be edited:

Anvitha, [10/19/2023 8:39 AM]
Date=22-Aug-2023 00:00,  Category=Work,  Amount=$24.0

MyExpenseBot, [10/19/2023 8:39 AM]
What do you want to update?

Anvitha, [10/19/2023 8:39 AM]
Category=Work

MyExpenseBot, [10/19/2023 8:39 AM]
Please select the new category

Anvitha, [10/19/2023 8:39 AM]
Volunteering

MyExpenseBot, [10/19/2023 8:39 AM]
Category is updated