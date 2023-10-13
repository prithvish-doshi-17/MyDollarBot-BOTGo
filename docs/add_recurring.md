# About MyDollarBot's /add_recurring Feature
This feature enables the user to add a new expense to their expense tracker.
Currently we have the following expense categories set by default:

- Food
- Groceries
- Utilities
- Transport
- Shopping
- Miscellaneous

The user can choose a an existing category or add custom category and add the amount they have spent to be stored in the expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/prithvish-doshi-17/MyDollarBot-BOTGo/blob/main/code/add_recurring.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the add feature. It pop ups a menu on the bot asking the user to choose their expense category, after which control is given to post_category_selection(message, bot) for further proccessing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main main.py function.

2. post_category_selection(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the add_recurring.py file. It requests the user to enter the amount they have spent on the expense category chosen and then passes control to post_amount_input(message, bot): for further processing.

3. post_amount_input(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the post_category_selection(message, bot): function in the add_recurring.py file. It takes the amount entered by the user, validates it with helper.validate() and then calls post_duration(message, bot): for further processing.

4. post_duration(message, bot):
 It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the post_amount_input(message, bot): function in the add_recurring.py file. It takes the duration entered by the user, validates it with helper.validate() and then calls add_user_record to store it.

5. add_user_record(chat_id, record_to_be_added):
 Takes 2 arguments - **chat_id** or the chat_id of the user's chat, and **record_to_be_added** which is the expense record to be added to the store. It then stores this expense record in the store.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add_recurring into the telegram bot.

Below you can see an example in text format:

dollarbot, [28.11.21 16:48]
[In reply to Prithvish Doshi]
Select Category

Prithvish Doshi, [28.11.21 16:48]
Food

dollarbot, [28.11.21 16:48]
How much did you spend on Food? 
(Enter numeric values only)

Prithvish Doshi, [28.11.21 16:48]
15

dollarbot, [28.11.21 16:48]
For how many months in the future will the expense be there?
(Enter integer values only)

Prithvish Doshi, [28.11.21 16:48]
6

dollarbot, [28.11.21 16:48]
The following expenditure has been recorded: You have spent $15.0 for Food for the next 6 months
