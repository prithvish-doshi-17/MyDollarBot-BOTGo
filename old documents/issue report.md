# Issue Report

Following were the issues for which the solutions were discussed before they were closed.

## 1) add budget horizontal lines in display - graphing
In the display function, there is an option to show a bar graph of expenditure. There, you would need to display a line indicating the budget.

If it's an overall budget, it should be a horizontal line through all categories.

If it's a category-wise, then it should be separate horizontal lines for each category.

Pass the budget to the plotting function. And each budget is plotted as a horizontal line and has the same color as the category bar of expense.


## 2) display budget in the display function - text
Along with the normal display function in text format, add at the top a line containing the current budget set by the user, whether it is an overall or category-wise budget.

Also, display the amount remaining for the current month in the budget under that.
Calculate the remaining amount of each budget when /display command is called.　I return the text format first and then return the picture format.
## 3) Add new recurring expense
Added a new file add_recurring.py which handles the cases of monthly recurring expenses.

## 4) View recurring expenses
/history command also shows the recurring expenses (in text output and graph output) in this version.

## 5) Add a command for recurring expense 
Command /add_recurring is added. It asks for Category, Amount and Duration (number of months) from the use and adds that particular recurring expense to the JSON file.

## 6) Add a new custom category 
The name of this should be taken from the user and the new category should be added to the user's data, and be updated in the master list of categories read from the helper module.
With the command "/category" the bot is able to manage categories now.
By entering "Add", we can add a custom category.

## 7) Add a new custom category

The name of this should be taken from the user and the new category should be added to the user's data, and be updated in the master list of categories read from the helper module.
With the command "/category" the bot is able to manage categories now.
By entering "Add", we can add a custom category.

## 8) Delete custom category

You should display all custom categories on the Telegram UI to the user, and they must pick one which should subsequently be removed.

We leave the option of removing all data associated with the category, or keeping it as a historical record to you.

With the command "/category" the bot is able to manage categories now.
By entering "Delete", we can add a custom category.

## 9) Adding pie chart in the display function 

Pie chart along with bar graph was added in the display command.

##10) Adding Histograms to compare previous month's spend.

/history command will now show the previous transaction history along with month wise transaction. The solution was being discuss before closing the issue.

## 11) Overlapping plots. 
The problem of overlapping plot was solve by adding plt.clf() code in every plotter function.

## 12) Older name of the application was displayed

The name was changed to :My Dollar Bot, however application name was older one.
Updated the codes for user experience.
 
## 13) Add testcase of category.py

Finished the file test_category.py.
Check the code coverage by the following command:
coverage run -m pytest test/
coverage report
