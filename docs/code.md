# About MyExpenseBot code.py file
code.py is the main file from where calls to the corresponding .py files for all features are sent. It contains a number of endpoints which redirect to function calls in the corresponding files. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/nainisha-b/MyExpenseBot/blob/test1/code/code.py)

# Code Description
## Functions

1. main()
The entire bot's execution begins here. It ensure the **bot** variable begins polling and actively listening for requests from telegram.

2. listener(user_requests):
Takes 1 argument **user_requests** and logs all user interaction with the bot including all bot commands run and any other issue logs.

3. start_and_menu_command(m):
Prints out the the main menu displaying the features that the bot offers and the corresponding commands to be run from the Telegram UI to use these features. Commands used to run this: commands=['start', 'menu']

4. command_add(message)
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls add.py to run to execute the add functionality. Commands used to run this: commands=['add']

5. command_add_recurring(message)
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls add_recurring.py to run to execute the functionality. Commands used to run this: commands=['add_recurring']

6. command_history(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls history.py to run to execute the add functionality. Commands used to run this: commands=['history']

7. command_edit(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls edit.py to run to execute the add functionality. Commands used to run this: commands=['edit']

8. command_display(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls display.py to run to execute the add functionality. Commands used to run this: commands=['display']

9. command_delete(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls delete.py to run to execute the add functionality. Commands used to run this: commands=['display']

10. command_estimate(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls estimate.py to run to execute the add functionality. Commands used to run this: commands=['estimate']

11. command_budget(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls budget.py to run to execute the add functionality. Commands used to run this: commands=['budget']

12. command_category(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls category.py to run to execute the add functionality. Commands used to run this: commands=['category']

13.command_category(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls pdf.py to run to execute the add functionality. Commands used to run this: commands=['pdf']

# How to run this feature?
This file contains information on the main code.py file from where all features are run. Instructions to run this are the same as instructions to run the project and can be found in README.md.
