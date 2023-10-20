# About MyExpenseBot /helper class
The helper file contains a set of functions that are commonly used for repeated tasks in the various features of MyDollarBot. Since these come up often, we have put them all up here in a separate file for reusability.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/nainisha-b/MyExpenseBot/blob/test1/code/helper.py)

# Code Description
## Functions

1. read_json():
Function to load .json expense record data

2. write_json(user_list):
Stores data into the datastore of the bot.

3. validate_entered_amount(amount_entered):
Takes 1 argument, **amount_entered**. It validates this amount's format to see if it has been correctly entered by the user.

4. validate_entered_date(date_entered):
Takes 1 argument, **date_entered**. It validates this date's format to see if it has been correctly entered by the user.

5. validate_entered_duration(duration_entered):
Takes 1 argument, **duration_entered**. It validates this date's format to see if it has been correctly entered by the user.

6. getUserIncomeHistory(chat_id):
Takes 1 argument **chat_id** and uses this to get the relevant user's income historical data.
   
7. getUserHistory(chat_id):
Takes 1 argument **chat_id** and uses this to get the relevant user's historical data.

8. getUserExpenseHistory(chat_id):
Takes 1 argument **chat_id** and uses this to get the relevant user's expense historical data.

9. getUserData(chat_id):
Takes 1 argument **chat_id** and uses this to get the relevant user's data.

10. getOverallBudget(chat_id):
Takes 1 argument **chat_id** and uses this to get the total budget.

11. getCategoryBudget(chatId):
Takes 1 argument **chatId** and uses this to get the budget of categories.

12. getCategoryBudgetByCategory(chatId, cat):
Takes 2 argument **chatId** **category** and uses this to get the budget of particular category.

13. canAddBudget(chatId):
Takes 1 argument **chatId** and uses this to know the possibility of adding budget.

14. isOverallBudgetAvailable(chatId):
Takes 1 argument **chatId** and checking whether the overall budget does exist or not.

15. isCategoryBudgetAvailable(chatId):
Takes 1 argument **chatId** and checking whether the category budget does exist or not.

16. isCategoryBudgetByCategoryAvailable(chatId, cat):
Takes 2 argument **chatId**,**category** and checking whether the category budget of a particular category does exist or not.

17. display_remaining_budget(message, bot, cat):
Takes 3 arguments **message**,**bot**,**category** to display the budget.

18.display_remaining_overall_budget(message, bot):
Takes 2 arguments **message**,**bot** to display remaining overall budget.

19. calculateRemainingOverallBudget(chat_id):
Takes 1 argument **chat_id** to calculate the budget stored in the history.

20. calculate_total_spendings(queryResult):
returns result of the total expenses.

21. display_remaining_category_budget(message, bot, cat):
Takes 3 arguments **message**,**bot**,**category** to display the category budget.

22. calculateRemainingCategoryBudget(chat_id, cat):
Takes 2 arguments **chat_id**,**category** to calculate the remaining category budget.

23. calculate_total_spendings_for_category(queryResult, cat):
returns the total spendings based on a particular category choosen. 

24. getSpendCategories():
This functions returns the spend categories used in the bot. These are defined the same file.

25. getIncomeCategories():
This function returns the income categories used in the bot defined in the file.

26. getCategories(selectedType):
This function returns the income categories if selectedType="Income" else returns spend categories.

27. getSpendDisplayOptions():
This functions returns the spend display options used in the bot. These are defined the same file.

28. getSpendEstimateOptions():
This functions returns the spend estimate options used in the bot. These are defined the same file.

29. getCommands():
This functions returns the command options used in the bot. These are defined the same file.

30. def getDateFormat():
This functions returns the date format used in the bot. 

31. def getTimeFormat():
This functions returns the time format used in the bot. 

32. def getMonthFormat():
This functions returns the month format used in the bot. 

33. def getplot():
This functions returns the different plots used in the bot. These are defined the same file.

34. def getChoices():
This function returns the choices used in bot

35. def getBudgetOptions():
This function returns budget_options in bot.

36. def getBudgetTypes():
This function returns budget_types in bot.

37. def getUpdateOptions():
The function returns update_options in bot.

38. def getCategoryOptions():
The function returns category_options in bot

39. def getIncomeOrExpense():
The function returns an option to choose income or expense.

40. def getCurrencyOptions():
THe function returns the different currency options for conversion.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.

This file is not a feature and cannot be run per se. Its functions are used all over by the other files as it provides helper functions for various functionalities and features.
