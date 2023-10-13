import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] // 2, y[i], ha='center')


def visualize(total_text, budgetData):
    # set the color for bars
    colors = ['red', 'cornflowerblue', 'greenyellow', 'orange', 'violet', 'grey']
    # plot the expense bar chart
    total_text_split = [line for line in total_text.split('\n') if line.strip() != '']
    categ_val = {}
    # summarize the expense by categories
    for i in total_text_split:
        a = i.split(' ')
        a[1] = a[1].replace("$", "")
        categ_val[a[0]] = float(a[1])

    # set categories as x-axis and amount as y-axis
    x = list(categ_val.keys())
    y = list(categ_val.values())

    plt.bar(categ_val.keys(), categ_val.values(), color=colors, edgecolor='black')
    addlabels(x, y)

    plt.ylabel("Expenditure")
    plt.xlabel("Categories")
    plt.xticks(rotation=45)

    # plot budget in the horizontal line format
    lines = []
    labels = []
    if isinstance(budgetData, str):
        # if budget data is str denoting it is overall budget
        lines.append(plt.axhline(y=float(budgetData), color="r", linestyle="-"))
        labels.append("overall budget")
    elif isinstance(budgetData, dict):
        # if budget data is dict denoting it is category budget
        colorCnt = 0
        # to avoid the budget override by each others, record the budget and adjust the position of the line
        duplicate = {}
        for key in budgetData.keys():
            val = budgetData[key]
            plotVal = float(val)
            if val in duplicate:
                # if duplicate, move line upwards
                plotVal += 2 * duplicate[val]
            lines.append(plt.axhline(y=plotVal, color=colors[colorCnt % len(colors)], linestyle="-"))

            # record the amount
            duplicate[val] = duplicate[val] + 1 if val in duplicate else 1
            labels.append(key)
            colorCnt += 1

    plt.legend(lines, labels)
    plt.savefig('expenditure.png', bbox_inches='tight')

    # clean the plot to avoid the old data remains on it
    plt.clf()
    plt.cla()
    plt.close()
    
def vis(total_text):
    total_text_split = [line for line in total_text.split('\n') if line.strip() != '']
    categ_val = {}
    for i in total_text_split:
        a = i.split(' ')
        a[1] = a[1].replace("$", "")
        categ_val[a[0]] = float(a[1])

    x = list(categ_val.keys())
    y = list(categ_val.values())
    
    ##plt.bar(categ_val.keys(), categ_val.values(), color=[(1.00, 0, 0, 0.6), (0.2, 0.4, 0.6, 0.6), (0, 1.00, 0, 0.6), (1.00, 1.00, 0, 1.00)], edgecolor='blue')
   ## addlabels(x, y)
    plt.clf()
    plt.pie(y, labels=x, autopct='%.1f%%')
    ##plt.ylabel("Categories")
    ##plt.xlabel("Expenditure")
    ##plt.xticks(rotation=90)

    plt.savefig('pie.png')


def viz(total_text):
    total_text_split = [line for line in total_text.split('\n') if line.strip() != '']
    categ_val = {}
    for i in total_text_split:
        a = i.split(' ')
        a[1] = a[1].replace("$", "")
        categ_val[a[0]] = float(a[1])

    x = list(categ_val.keys())
    y = list(categ_val.values())
    plt.clf()
    plt.bar(categ_val.keys(), categ_val.values(), color=[(1.00, 0, 0, 0.6), (0.2, 0.4, 0.6, 0.6), (0, 1.00, 0, 0.6), (1.00, 1.00, 0, 1.00)], edgecolor='blue')
    addlabels(x, y)

    plt.ylabel("Categories")
    plt.xlabel("Expenditure")
    plt.xticks(rotation=45)

    plt.savefig('expend.png', bbox_inches='tight')