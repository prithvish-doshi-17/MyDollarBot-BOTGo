from flask import Flask
import json
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def landing():
    return "Hello World!"



@app.route('/dummyData')
def data(): 
    # Sample data for testing
    data =  [
        {"category": "Food", "allocated": 500, "spent": 300, "remaining": 200},
        {"category": "Rent", "allocated": 1000, "spent": 1000, "remaining": 0},
        {"category": "Entertainment", "allocated": 100, "spent": 50, "remaining": 50}
    ]
    return json.dumps(data)


@app.route('/budgets')
def budgets():
    # Sample data for testing
    budgets = [
        {"category": "Food", "allocated": 500, "spent": 300, "remaining": 200},
        {"category": "Rent", "allocated": 1000, "spent": 1000, "remaining": 0},
        {"category": "Entertainment", "allocated": 100, "spent": 50, "remaining": 50}
    ]
    return jsonify(budgets)

if __name__ == '__main__':
    app.run(debug=True)