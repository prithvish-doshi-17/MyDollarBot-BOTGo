import helper
import logging
from telebot import types


def run(message, bot):
    chat_id = message.chat.id
    if helper.isOverallBudgetAvailable(chat_id):
        update_overall_budget(chat_id, bot)
    elif helper.isCategoryBudgetAvailable(chat_id):
        update_category_budget(message, bot)
    else:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        options = helper.getBudgetTypes()
        markup.row_width = 2
        for c in options.values():
            markup.add(c)
        msg = bot.reply_to(message, 'Select Budget Type', reply_markup=markup)
        bot.register_next_step_handler(msg, post_type_selection, bot)


def post_type_selection(message, bot):
    try:
        chat_id = message.chat.id
        op = message.text
        options = helper.getBudgetTypes()
        if op not in options.values():
            bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
            raise Exception("Sorry I don't recognise this operation \"{}\"!".format(op))
        if op == options['overall']:
            update_overall_budget(chat_id, bot)
        elif op == options['category']:
            update_category_budget(message, bot)
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)


def update_overall_budget(chat_id, bot):
    if (helper.isOverallBudgetAvailable(chat_id)):
        currentBudget = helper.getOverallBudget(chat_id)
        msg_string = 'Current Budget is ${}\n\nHow much is your new monthly budget? \n(Enter numeric values only)'
        message = bot.send_message(chat_id, msg_string.format(currentBudget))
    else:
        message = bot.send_message(chat_id, 'How much is your monthly budget? \n(Enter numeric values only)')
    bot.register_next_step_handler(message, post_overall_amount_input, bot)


def post_overall_amount_input(message, bot):
    try:
        chat_id = message.chat.id
        amount_value = helper.validate_entered_amount(message.text)
        if amount_value == 0:
            raise Exception("Invalid amount.")
        user_list = helper.read_json()
        if str(chat_id) not in user_list:
            user_list[str(chat_id)] = helper.createNewUserRecord()
        user_list[str(chat_id)]['budget']['overall'] = amount_value
        helper.write_json(user_list)
        bot.send_message(chat_id, 'Budget Updated!')
        return user_list
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)


def update_category_budget(message, bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    categories = helper.getSpendCategories()
    markup.row_width = 2
    for c in categories:
        markup.add(c)
    msg = bot.reply_to(message, 'Select Category', reply_markup=markup)
    bot.register_next_step_handler(msg, post_category_selection, bot)


def post_category_selection(message, bot):
    try:
        chat_id = message.chat.id
        selected_category = message.text
        categories = helper.getSpendCategories()
        if selected_category not in categories:
            bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
            raise Exception("Sorry I don't recognise this category \"{}\"!".format(selected_category))
        if helper.isCategoryBudgetByCategoryAvailable(chat_id, selected_category):
            currentBudget = helper.getCategoryBudgetByCategory(chat_id, selected_category)
            msg_string = 'Current monthly budget for {} is {}\n\nEnter monthly budget for {}\n(Enter numeric values only)'
            message = bot.send_message(chat_id, msg_string.format(selected_category, currentBudget, selected_category))
        else:
            message = bot.send_message(chat_id, 'Enter monthly budget for ' + selected_category + '\n(Enter numeric values only)')
        bot.register_next_step_handler(message, post_category_amount_input, bot, selected_category)
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)


def post_category_amount_input(message, bot, category):
    try:
        chat_id = message.chat.id
        amount_value = helper.validate_entered_amount(message.text)
        if amount_value == 0:
            raise Exception("Invalid amount.")
        user_list = helper.read_json()
        if str(chat_id) not in user_list:
            user_list[str(chat_id)] = helper.createNewUserRecord()
        if user_list[str(chat_id)]['budget']['category'] is None:
            user_list[str(chat_id)]['budget']['category'] = {}
        user_list[str(chat_id)]['budget']['category'][category] = amount_value
        helper.write_json(user_list)
        message = bot.send_message(chat_id, 'Budget for ' + category + ' Created!')
        post_category_add(message, bot)

    except Exception as e:
        helper.throw_exception(e, message, bot, logging)


def post_category_add(message, bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    options = helper.getUpdateOptions().values()
    markup.row_width = 2
    for c in options:
        markup.add(c)
    msg = bot.reply_to(message, 'Select Option', reply_markup=markup)
    bot.register_next_step_handler(msg, post_option_selection, bot)


def post_option_selection(message, bot):
    print("here")
    selected_option = message.text
    options = helper.getUpdateOptions()
    print("here")
    if selected_option == options['continue']:
        update_category_budget(message, bot)
