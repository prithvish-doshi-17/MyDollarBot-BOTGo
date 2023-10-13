import re
import helper
from telebot import types


def run(m, bot):
    chat_id = m.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    for c in helper.getUserHistory(chat_id):
        expense_data = c.split(',')
        str_date = "Date=" + expense_data[0]
        str_category = ",\t\tCategory=" + expense_data[1]
        str_amount = ",\t\tAmount=$" + expense_data[2]
        markup.add(str_date + str_category + str_amount)
    info = bot.reply_to(m, "Select expense to be edited:", reply_markup=markup)
    bot.register_next_step_handler(info, select_category_to_be_updated, bot)


def select_category_to_be_updated(m, bot):
    info = m.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    selected_data = [] if info is None else info.split(',')
    for c in selected_data:
        markup.add(c.strip())
    choice = bot.reply_to(m, "What do you want to update?", reply_markup=markup)
    bot.register_next_step_handler(choice, enter_updated_data, bot, selected_data)


def enter_updated_data(m, bot, selected_data):
    choice1 = "" if m.text is None else m.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    for cat in helper.getSpendCategories():
        markup.add(cat)

    if 'Date' in choice1:
        new_date = bot.reply_to(m, "Please enter the new date (in dd-mmm-yyy format)")
        bot.register_next_step_handler(new_date, edit_date, bot, selected_data)

    if 'Category' in choice1:
        new_cat = bot.reply_to(m, "Please select the new category", reply_markup=markup)
        bot.register_next_step_handler(new_cat, edit_cat, bot, selected_data)

    if 'Amount' in choice1:
        new_cost = bot.reply_to(m, "Please type the new cost")
        bot.register_next_step_handler(new_cost, edit_cost, bot, selected_data)


def edit_date(m, bot, selected_data):
    user_list = helper.read_json()
    new_date = "" if m.text is None else m.text
    date_format = r'^(([0][1-9])|([1-2][0-9])|([3][0-1]))\-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\-\d{4}$'
    x1 = re.search(date_format, new_date)
    if x1 is None:
        bot.reply_to(m, "The date is incorrect")
        return
    chat_id = m.chat.id
    data_edit = helper.getUserHistory(chat_id)
    for i in range(len(data_edit)):
        user_data = data_edit[i].split(',')
        selected_date = selected_data[0].split('=')[1]
        selected_category = selected_data[1].split('=')[1]
        selected_amount = selected_data[2].split('=')[1]
        if user_data[0] == selected_date and user_data[1] == selected_category and user_data[2] == selected_amount[1:]:
            data_edit[i] = new_date + ',' + selected_category + ',' + selected_amount[1:]
            break

    user_list[str(chat_id)]['data'] = data_edit
    helper.write_json(user_list)
    bot.reply_to(m, "Date is updated")


def edit_cat(m, bot, selected_data):
    user_list = helper.read_json()
    chat_id = m.chat.id
    data_edit = helper.getUserHistory(chat_id)
    new_cat = "" if m.text is None else m.text
    for i in range(len(data_edit)):
        user_data = data_edit[i].split(',')
        selected_date = selected_data[0].split('=')[1]
        selected_category = selected_data[1].split('=')[1]
        selected_amount = selected_data[2].split('=')[1]
        if user_data[0] == selected_date and user_data[1] == selected_category and user_data[2] == selected_amount[1:]:
            data_edit[i] = selected_date + ',' + new_cat + ',' + selected_amount[1:]
            break

    user_list[str(chat_id)]['data'] = data_edit
    helper.write_json(user_list)
    bot.reply_to(m, "Category is updated")


def edit_cost(m, bot, selected_data):
    user_list = helper.read_json()
    new_cost = "" if m.text is None else m.text
    chat_id = m.chat.id
    data_edit = helper.getUserHistory(chat_id)

    if helper.validate_entered_amount(new_cost) != 0:
        for i in range(len(data_edit)):
            user_data = data_edit[i].split(',')
            selected_date = selected_data[0].split('=')[1]
            selected_category = selected_data[1].split('=')[1]
            selected_amount = selected_data[2].split('=')[1]
            if user_data[0] == selected_date and user_data[1] == selected_category and user_data[2] == selected_amount[1:]:
                data_edit[i] = selected_date + ',' + selected_category + ',' + new_cost
                break
        user_list[str(chat_id)]['data'] = data_edit
        helper.write_json(user_list)
        bot.reply_to(m, "Expense amount is updated")
    else:
        bot.reply_to(m, "The cost is invalid")
        return
