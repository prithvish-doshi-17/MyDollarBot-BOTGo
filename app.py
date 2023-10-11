from flask import Flask, render_template
# from budget_view import display_overall_budget as fetch_budget
app = Flask(__name__)

# @app.route('/budget')
# def budget():
#     budget = fetch_budget()
#     return render_template('budget.html', budget=budget)

@app.route('/')
def landing():
    return render_template('landing_page.html')


@app.route('/budgets')
def budgets():
    # Sample data for testing
    budgets = [
        {"category": "Food", "allocated": 500, "spent": 300, "remaining": 200},
        {"category": "Rent", "allocated": 1000, "spent": 1000, "remaining": 0},
        {"category": "Entertainment", "allocated": 100, "spent": 50, "remaining": 50}
    ]
    return render_template('budget.html', budgets=budgets)

if __name__ == '__main__':
    app.run(debug=True)