from flask import Flask
import json
from flask import jsonify, request
import helper
from add import add_user_record
from datetime import datetime
import budget_view

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)