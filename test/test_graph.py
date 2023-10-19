from main import graphing
from mock import ANY

dummy_total_text_none = ""
dummy_total_text_data = """Food $10.0
Transport $50.0
Shopping $148.0
Miscellaneous $47.93
Utilities $200.0
Groceries $55.21\n"""
dummy_budget = "100.0"

dummy_x = ['Food', 'Transport', 'Shopping', 'Miscellaneous', 'Utilities', 'Groceries']
dummy_y = [10.0, 50.0, 148.0, 47.93, 200.0, 55.21]
dummy_categ_val = {'Food': 10.0, 'Transport': 50.0, 'Shopping': 148.0, 'Miscellaneous': 47.93, 'Miscellaneous': 47.93, 'Utilities': 200.0, 'Groceries': 55.21}
dummy_color = ['red','cornflowerblue','greenyellow','orange','violet','grey']
dummy_edgecolor = 'black'


def test_visualize(mocker):
    mocker.patch.object(graphing, 'plt')
    graphing.plt.bar.return_value = True
    graphing.visualize(dummy_total_text_data, dummy_budget)
    graphing.plt.bar.assert_called_with(dummy_categ_val.keys(), ANY, color=dummy_color, edgecolor=dummy_edgecolor)
