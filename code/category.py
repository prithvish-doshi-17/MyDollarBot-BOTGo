import helper
import logging
from telebot import types

# The main funtion of category.py.
# User can start to manage their categories after calling it
def run(message, bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    options = helper.getIncomeOrExpense()
    markup.row_width = 2
    for c in options.values():
        markup.add(c)
    msg = bot.reply_to(message, 'Select Income or Expense', reply_markup=markup)
    bot.register_next_step_handler(msg, post_type_selection, bot)

def post_type_selection(message, bot):
    try:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        chat_id = message.chat.id
        selectedType = message.text
        options1 = helper.getCategoryOptions()
        markup.row_width = 2
        for c in options1.values():
            markup.add(c)
        msg = bot.reply_to(message, 'Select operation', reply_markup=markup)
        bot.register_next_step_handler(msg, post_operation_selection, bot, selectedType)
    except Exception as e:
        # print("hit exception")
        helper.throw_exception(e, message, bot, logging)


# User have three funtionaliy can choose, add a category, delete a category or view the current categories
def post_operation_selection(message, bot, selectedType):
    try:
        chat_id = message.chat.id
        op = message.text
        options = helper.getCategoryOptions()
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        # Handle the exception of unknown operation 
        if op not in options.values():
            bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
            raise Exception("Sorry I don't recognise this operation \"{}\"!".format(op))
        if op == options['add']:
            msg = bot.reply_to(message, 'Please type the new category name')
            bot.register_next_step_handler(msg, category_add, bot, selectedType)
        elif op == options['view']:
            category_view(message, bot, selectedType)
        elif op == options['delete']:
            markup.row_width = 2
            for c in helper.getCategories(selectedType):
                markup.add(c)
            # Handle the exception of trying to delete the last category
            if len(helper.getCategories(selectedType)) <= 1:
                bot.send_message(chat_id, 'Invalid', reply_markup=types.ReplyKeyboardRemove())
                raise Exception("Number of categories cannot be zero.")
            else:
                msg = bot.reply_to(message, 'Please choose the category you want to delete', reply_markup=markup)
                bot.register_next_step_handler(msg, category_delete, bot, selectedType)
    except Exception as e:
        # print("hit exception")
        helper.throw_exception(e, message, bot, logging)
    
# Use the funtion to add a new category 
def category_add(message, bot, selectedType):
    chat_id = message.chat.id
    category_name = message.text
    if selectedType == "Income" :
        file_name = "income_categories.txt"
    else:
        file_name = "categories.txt"
    with open(file_name, "r") as tf:
        lines = tf.read().split(',')
        tf.close()
    f = open(file_name, "a")   
    if lines == ['']:
        f.write(category_name)    
    else:
        f.write(',' + category_name)
    f.close()
    bot.send_message(chat_id, 'Add category "{}" successfully!'.format(category_name))

# Use the funciton to view all of the categories in chat room
def category_view(message, bot, selectedType):
    chat_id = message.chat.id
    if selectedType == "Income" :
        file_name = "income_categories.txt"
    else:
        file_name = "categories.txt"
    with open(file_name, "r") as tf:
        lines = tf.read()
        tf.close()
    bot.send_message(chat_id, 'The categories are:\n{}'.format(lines))

# Use the funtion to delete a category
def category_delete(message, bot, selectedType):
    chat_id = message.chat.id
    category_name = message.text
    find_to_delete = False
    if selectedType == "Income" :
        file_name = "income_categories.txt"
    else:
        file_name = "categories.txt"
    with open(file_name, "r") as tf:
        categories = tf.read().split(',')
        tf.close()
    for category in categories:
        if category == '':
            categories.remove('')            
        if category == category_name:
            find_to_delete = True
            categories.remove(category)
    # Handle the exception of deleting a not exist category
    if find_to_delete == False:
        bot.send_message(chat_id, 'Cannot find the category QAQ', reply_markup=types.ReplyKeyboardRemove())
    elif find_to_delete:
        f = open(file_name, "w")   
        for category in categories:
            if category == categories[0]:
                f.write(category)
            else:   
                f.write("," + category)
        f.close()
        bot.send_message(chat_id, 'Delete category "{}" successfully!'.format(category_name))
        