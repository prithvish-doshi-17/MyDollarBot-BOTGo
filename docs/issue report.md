# Issue Report

Following were the issues for which the solutions were discussed before they were closed.

## 1) Add features to record users income
In the add function, there is only option to add the amount value as a part of expenditure previously. But we need an option to add income amount to track the budget of an user, which gives the clear view for user to track theie income, expenditure
and their budget. 

Adding a menu option to select the type of amount they are adding i.e., income or expense before they enter the amount will help user to track amounts in income or expense. This helps the user to track the user to have both income and expense history.

## 2) Add features to record users recurring income
Similar to adding the income once, user might want to add the recurring income such as monthly or biweekly salary without adding it every month manually. Add recurring income helps the user to add income peroidically without multiple user input. The function for this is present in add_recurring file. 

## 3) Feature for cashflow graphs
Added the cashflow graphs to show the flow of income, expense and budget to the user so that user can easily understand their periodic budget and expenditure visually.

## 4) Feature to add manual date using calendar
Included a new module telegram-bot-calendar to invoke the inbuilt calendar feature in telegram so that user can record an income or expenditure for any date through user friendly calendar and update it whenever user wants to update the date without adding any restrictions to the user.

## 5) Display user history in descending order and apply formatting
Added a sort functionality to sort the dates in the descending order so that income or expense history gives the clear picture to the user about the income or expenditure no matter when they add the new income or expense for the amount they spent and formatted it accordingly.

## 6) Allow user to add different currency input
Previously we were only recording the expenditure value in dollar but we added 2 more currencies i.e., euros and INR to give user a flexibility to add the income or expenditure in different currency input when taking the input in add file.

## 7) Ensure user can see cashflow graphs for past 12 months

In cashflow graphs shows all the combined data irrespective of which year they spent on so we added a restriction to show the graph for only past 12 months to eliminate the past data and show the relevant data to the user. 

## 8) Update edit methods with all the latest changes

Updated all the changes which were made in add module i.e., taking a date input using calendar, updating the record of income or expense in the similar way as adding the income or expense record in edit file.

## 9) Fix Testcases 

Updated the testcases to the changes made to the file in the code so that test suite can run smoothly without encountering any errors.

## 10) Update documentation

Documentation has been updated to give the clear picture of the changes which we made and give better understanding about the features to the users and developers.

## 11) Create a video depicting the new features addition
Created a video explaining the new features which has been added on the top of the existing features to give the better understanding of the features implemented.
