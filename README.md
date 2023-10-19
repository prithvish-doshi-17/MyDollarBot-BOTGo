# 💰 TrackMyDollar V2.0 - Budget On The Go(BOTGo) 💰

Link to delta of Phase 3 - <https://drive.google.com/file/d/1VqQPTm4tFjG8mbixrjqvjnmgsYb8YD49/view?usp=sharing>

This video shows only the new features and enhancement of some older features. All the other features from phase 2 are working as it is.

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
[![GitHub contributors](https://img.shields.io/github/contributors/prithvish-doshi-17/MyDollarBot-BOTGo)](https://github.com/prithvish-doshi-17/MyDollarBot-BOTGo/graphs/contributors)
[![DOI](https://zenodo.org/badge/414661894.svg)](https://zenodo.org/badge/latestdoi/414661894)
[![Build Status](https://app.travis-ci.com/sak007/MyDollarBot-BOTGo.svg?branch=main)](https://app.travis-ci.com/github/sak007/MyDollarBot-BOTGo)
[![codecov](https://codecov.io/gh/sak007/MyDollarBot-BOTGo/branch/main/graph/badge.svg?token=5AYMR8MNMP)](https://codecov.io/gh/sak007/MyDollarBot-BOTGo)
[![GitHub issues](https://img.shields.io/github/issues/prithvish-doshi-17/MyDollarBot-BOTGo)](https://github.com/prithvish-doshi-17/MyDollarBot-BOTGo/issues?q=is%3Aopen+is%3Aissue)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/prithvish-doshi-17/MyDollarBot-BOTGo)](https://github.com/prithvish-doshi-17/MyDollarBot-BOTGo/issues?q=is%3Aissue+is%3Aclosed)

![Fork](https://img.shields.io/github/forks/deekay2310/MyDollarBot?style=social)

## About TrackMyDollar

TrackMyDollar is an easy-to-use Telegram Bot that assists you in recording your daily expenses on a local system without any hassle
With simple commands, this bot allows you to:

*   Add/Record a new spending

*   Show the sum of your expenditure for the current day/month

*   Display your spending history

*   Clear/Erase all your records

*   Edit/Change any spending details if you wish to

## What's new? (From Phase 2 to Phase 3)

*   Recurring expense:
    Add a recurring expense that adds a certain amount every month to the user's spending, for any given category.

*   Custom category:
    User can add a new category and delete an existing category as per the needs

*   Budgeting:
    User can see the budget value for the total expense and/or for each of the existing categories in the /display function

*   Better visualization:
    Added pie charts, bar graphs with and without budget lines for the user to have a look at the spending history in a better manner
    Added bar graph in the /history command to see spending across different categories
    User can see the daily and monthly expenses for spending history

*   Deployment on GCP (the bot is now available, and can be used on any device by searching for @testforbudgetmanagerbot on Telegram)

## What more can be done?

Please refer to the issue list available [here](https://github.com/prithvish-doshi-17/MyDollarBot-BOTGo/issues) to see what more can be done to make MyDollarBot better. Please refer to the MyDollarBot project present [here](https://github.com/prithvish-doshi-17/MyDollarBot-BOTGo/projects) to have a look at the tasks to be done, tasks currently in progress and tasks already done.

## Demo

<https://user-images.githubusercontent.com/72677919/140454147-f879010a-173b-47b9-9cfb-a389171924de.mp4>

## Installation guide

The below instructions can be followed in order to set-up this bot at your end in a span of few minutes! Let's get started:

1.  Clone this repository to your local system.

2.  Start a terminal session in the directory where the project has been cloned. Run the following command to install the required dependencies:

<!---->

      pip install -r requirements.txt

1.  In Telegram, search for "BotFather". Click on "Start", and enter the following command:

<!---->

      /newbot

Follow the instructions on screen and choose a name for your bot. After this, select a username for your bot that ends with "bot".

1.  BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy and save this token for future use.

2.  In the directory where this repo has been cloned, please run the below command to execute a bash script to run the Telegram Bot:

<!---->

       ./run.sh

(OR)

       bash run.sh

Please note that it will ask you to paste the API token you received from Telegram in step 4.
A successful run will generate a message on your terminal that says "TeleBot: Started polling."

1.  In the Telegram app, search for your newly created bot by entering the username and open the same. Now, on Telegram, enter the "/start" or "/menu" command, and you are all set to track your expenses!

## Testing

We use pytest to perform testing on all unit tests together. The command needs to be run from the home directory of the project. The command is:

    python run -m pytest test/

## Code Coverage

Code coverage is part of the build. Every time new code is pushed to the repository, the build is run, and along with it, code coverage is computed. This can be viewed by selecting the build, and then choosing the codecov pop-up on hover.

Locally, we use the coverage package in python for code coverage. The commands to check code coverage in python are as follows:

    coverage run -m pytest test/
    coverage report

## Notes:

You can download and install the Telegram desktop application for your system from the following site: <https://desktop.telegram.org/>
