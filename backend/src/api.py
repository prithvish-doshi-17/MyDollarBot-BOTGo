from flask import Flask
from flask import jsonify, request
# from budget_view import budget
import telebot
from collections import namedtuple
import logging
from add import run, add_user_record, post_category_selection, post_amount_input
import json

from jproperties import Properties

configs = Properties()

with open('user.properties', 'rb') as read_prop:
    configs.load(read_prop)

api_token = str(configs.get('api_token').data)

bot = telebot.TeleBot(api_token)

telebot.logger.setLevel(logging.INFO)

option = {}

app = Flask(__name__)

# functions for creating an artificial message so that its still synced with the bot
def dict_to_obj(data):
    return namedtuple('GenericDict', data.keys())(**data)

def create_message(userid, category):
    # Simulate a message object for the run function
    chat = {'id': userid}
    chat = dict_to_obj(chat)
    message = {'chat': chat, 'message_id': 1, 'text': category}
    message = dict_to_obj(message)
    return message

@app.route('/')
def landing():
    return "Hello World!"

@app.route('/dummyData')
def data(): 
    # Budget data
    budget_data = [
        {"category": "Food", "allocated": 500, "spent": 300, "remaining": 200},
        {"category": "Rent", "allocated": 1000, "spent": 1000, "remaining": 0},
        {"category": "Entertainment", "allocated": 100, "spent": 50, "remaining": 50},
        # ... Add other categories as needed
    ]

    # Individual spending data
    spendings = [
        {"category": "Food", "amount": 50, "description": "Dinner at ABC restaurant", "date": "2023-10-01"},
        {"category": "Food", "amount": 30, "description": "Groceries", "date": "2023-10-02"},
        {"category": "Entertainment", "amount": 50, "description": "Movie tickets", "date": "2023-10-03"},
        # ... Add other spendings as needed
    ]

    # Categories
    categories = [
        {"id": 1, "name": "Food"},
        {"id": 2, "name": "Rent"},
        {"id": 3, "name": "Entertainment"},
        # ... Add other categories as needed
    ]

    # Combine all data into one object
    data = {
        "budget_data": budget_data,
        "spendings": spendings,
        "categories": categories,
        # ... Add other data structures as needed
    }

    return jsonify(data)


@app.route('/budgets')
def budgets():
    # # Sample data for testing
    # budgets = [
    #     {"category": "Food", "allocated": 500, "spent": 300, "remaining": 200},
    #     {"category": "Rent", "allocated": 1000, "spent": 1000, "remaining": 0},
    #     {"category": "Entertainment", "allocated": 100, "spent": 50, "remaining": 50}
    # ]

    return jsonify(budgets)



@app.route('/add', methods=['POST'])
def add_expenditure():
    print(request.json)
    user_id = request.json.get('user_id')

    # create the message 
    message = create_message(user_id, "")

    print(message) 
    categories = run(message, bot)  # We can pass None for the bot parameter as it's not used here
    return jsonify({"categories": categories})


@app.route('/select-category', methods=['POST'])
def select_category():
    user_id = request.json.get('user_id')
    selected_category = request.json.get('category')
    # Simulate a message object for the post_category_selection function
    message = create_message(user_id, selected_category)
    response = post_category_selection(message, bot)
    return jsonify(response)

@app.route('/input-amount', methods=['POST'])
def input_amount():
    user_id = request.json.get('user_id')
    selected_category = request.json.get('category')
    amount = request.json.get('amount')
    # Simulate a message object for the post_amount_input function

    message = create_message(user_id, amount)
    response = post_amount_input(message, bot, selected_category)
    return jsonify(response)

@app.route("/all-budget-data", methods=['GET'])
def get_all_data():
    user_id = request.json.get('user_id')

    # open expense_record.json 
    with open('expense_record.json', 'r') as f:
        data = f.read()

    # parse file
    obj = json.loads(data)

    # look for the user_id and return the data
    if obj[user_id] != None:
        return jsonify(obj[user_id])
    else: 
        return jsonify({"message": "user not found"})
    
@app.route("/all-categories", methods=['GET'])
def get_all_categories():
    # open categories.txt
    with open('categories.txt', 'r') as f:
        data = f.read()

    # split each line using the comma as a delimeter 
    data = data.split(',')

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)