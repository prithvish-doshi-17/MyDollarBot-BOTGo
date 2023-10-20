# About MyExpenseBot's /display Feature's Graph module
This feature enables the user to see their expense in a graphical format to enable better UX.

Currently, the /display command will provide the expenses as a message to the users via the bot. To better the UX, we have added the option to show the expenses in a Bar Graph and pie chart along with budget line.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/nainisha-b/MyExpenseBot/blob/main/code/graphing.py)

# Code Description
## Functions

1. visualize(total_text, budgetData):
This is the main function used to implement the graphing part of display feature. This file is called from display.py. It takes two arguements- which **total_text** is the user history expense fo a user and **budgetData** is the user's budget settings. It creates a graph into the directory which is the return value of display.py.
2. addlabels(x, y):
This function is used to add the labels to the graph. It takes the expense values and adds the values inside the bar graph for each expense type.
3.vis(total_text):
This function takes total text as input and creates a pie chart based on the user's expense history and return a plotted pie chart.
4. viz(total_text):
This function takes total text as input and creates a bar chart without budget line based on the user's expense history and return a plotted bar chart.

# How to run this feature?
After you've added sufficient input data, use the /display command and you can see the output in a pictorial representation. 
