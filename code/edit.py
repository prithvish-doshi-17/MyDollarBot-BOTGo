import re
import helper
from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

def run(m, bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    options = helper.getIncomeOrExpense()
    markup.row_width = 2
    for c in options.values():
        markup.add(c)
    msg = bot.reply_to(m, 'Edit Income or Expense History', reply_markup=markup)
    bot.register_next_step_handler(msg, select_income_or_expense_to_be_edited, bot)

def select_income_or_expense_to_be_edited(msg, bot):
    chat_id = msg.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    selectedType = msg.text
    if(selectedType == "Income"):
        for c in helper.getUserIncomeHistory(chat_id):
            income_data = c.split(',')
            str_date = "Date=" + income_data[0]
            str_category = ",\t\tCategory=" + income_data[1]
            str_amount = ",\t\tAmount=$" + income_data[2]
            markup.add(str_date + str_category + str_amount)
    else:
        for c in helper.getUserExpenseHistory(chat_id):
            expense_data = c.split(',')
            str_date = "Date=" + expense_data[0]
            str_category = ",\t\tCategory=" + expense_data[1]
            str_amount = ",\t\tAmount=$" + expense_data[2]
            markup.add(str_date + str_category + str_amount)

    info = bot.reply_to(msg, "Select income/expense to be edited:", reply_markup=markup)
    bot.register_next_step_handler(info, select_category_to_be_updated, bot, selectedType)


def select_category_to_be_updated(m, bot, selectedType):
    info = m.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    selected_data = [] if info is None else info.split(',')
    for c in selected_data:
        markup.add(c.strip())
    choice = bot.reply_to(m, "What do you want to update?", reply_markup=markup)
    bot.register_next_step_handler(choice, enter_updated_data, bot, selected_data, selectedType)


def enter_updated_data(m, bot, selected_data, selectedType):
    choice1 = "" if m.text is None else m.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    if(selectedType == "Income"):
        for cat in helper.getIncomeCategories():
            markup.add(cat)
    else:
        for cat in helper.getSpendCategories():
            markup.add(cat)

    if 'Date' in choice1:
        calendar, step = DetailedTelegramCalendar().build()
        bot.send_message(m.chat.id, "Select a new date")
        bot.send_message(m.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar)

        @bot.callback_query_handler(func=DetailedTelegramCalendar.func())
        def cal(c):
            result, key, step = DetailedTelegramCalendar().process(c.data)

            if not result and key:
                bot.edit_message_text(
                    f"Select {LSTEP[step]}",
                    c.message.chat.id,
                    c.message.message_id,
                    reply_markup=key,
                )
            elif result:

                edit_date(c.message, bot, selected_data, selectedType, result)

                bot.edit_message_text(
                    f"Date is updated: {result}",
                    c.message.chat.id,
                    c.message.message_id,
                )

    if 'Category' in choice1:
        new_cat = bot.reply_to(m, "Please select the new category", reply_markup=markup)
        bot.register_next_step_handler(new_cat, edit_cat, bot, selected_data, selectedType)

    if 'Amount' in choice1:
        new_cost = bot.reply_to(m, "Please type the new cost")
        bot.register_next_step_handler(new_cost, edit_cost, bot, selected_data, selectedType)


def edit_date(m, bot, selected_data, selectedType,result):
    user_list = helper.read_json()
    new_date = str(helper.validate_entered_date(result))

    chat_id = m.chat.id
    data_edit = helper.getUserHistory(chat_id, selectedType)
    for i in range(len(data_edit)):
        user_data = data_edit[i].split(",")
        selected_date = selected_data[0].split("=")[1]
        selected_category = selected_data[1].split("=")[1]
        selected_amount = selected_data[2].split("=")[1]
        if (
            user_data[0] == selected_date and user_data[1] == selected_category and user_data[2] == selected_amount[1:]
        ):
            data_edit[i] = (
                new_date + "," + selected_category + "," + selected_amount[1:]
            )
            break
    if selectedType == "Income":
            user_list[str(chat_id)]['income_data'] = data_edit
            helper.write_json(user_list)
    else:
            user_list[str(chat_id)]['expense_data'] = data_edit
            helper.write_json(user_list)
    bot.reply_to(m, "Date is updated")


def edit_cat(m, bot, selected_data, selectedType):
    user_list = helper.read_json()
    chat_id = m.chat.id
    data_edit = helper.getUserHistory(chat_id, selectedType)
    new_cat = "" if m.text is None else m.text
    for i in range(len(data_edit)):
        user_data = data_edit[i].split(',')
        selected_date = selected_data[0].split('=')[1]
        selected_category = selected_data[1].split('=')[1]
        selected_amount = selected_data[2].split('=')[1]
        if user_data[0] == selected_date and user_data[1] == selected_category and user_data[2] == selected_amount[1:]:
            data_edit[i] = selected_date + ',' + new_cat + ',' + selected_amount[1:]
            break

    if selectedType == "Income":
            user_list[str(chat_id)]['income_data'] = data_edit
            helper.write_json(user_list)
    else:
            user_list[str(chat_id)]['expense_data'] = data_edit
            helper.write_json(user_list)
    bot.reply_to(m, "Category is updated")


def edit_cost(m, bot, selected_data, selectedType):
    user_list = helper.read_json()
    new_cost = "" if m.text is None else m.text
    chat_id = m.chat.id
    data_edit = helper.getUserHistory(chat_id, selectedType)

    if helper.validate_entered_amount(new_cost) != 0:
        for i in range(len(data_edit)):
            user_data = data_edit[i].split(',')
            selected_date = selected_data[0].split('=')[1]
            selected_category = selected_data[1].split('=')[1]
            selected_amount = selected_data[2].split('=')[1]
            if user_data[0] == selected_date and user_data[1] == selected_category and user_data[2] == selected_amount[1:]:
                data_edit[i] = selected_date + ',' + selected_category + ',' + new_cost
                break
        if selectedType == "Income":
            user_list[str(chat_id)]['income_data'] = data_edit
            helper.write_json(user_list)
            bot.reply_to(m, "Income amount is updated")
        else:
            user_list[str(chat_id)]['expense_data'] = data_edit
            helper.write_json(user_list)
            bot.reply_to(m, "Expense amount is updated")
    else:
        bot.reply_to(m, "The cost is invalid")
        return
