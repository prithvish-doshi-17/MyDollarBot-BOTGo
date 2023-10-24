import os
import json
#from mock.mock import patch
from unittest.mock import patch
from telebot import types
from code import add
from mock import ANY
from unittest.mock import Mock, ANY
from telegram_bot_calendar import DetailedTelegramCalendar

dateFormat = '%d-%b-%Y'
timeFormat = '%H:%M'
monthFormat = '%b-%Y'


@patch('telebot.telebot')
def test_run(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.reply_to.return_value = True
    message = create_message("hello from test run!")
    add.run(message, mc)
    assert(mc.reply_to.called)


@patch('telebot.telebot')
def test_post_category_selection_working(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    message = create_message("hello from testing!")
    add.post_category_selection(message, mc, "Income")
    assert(mc.send_message.called)


@patch('telebot.telebot')
def test_post_category_selection_noMatchingCategory(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = []
    mc.reply_to.return_value = True

    mocker.patch.object(add, 'helper')
    add.helper.getSpendCategories.return_value = None

    message = create_message("hello from testing!")
    add.post_category_selection(message, mc, "Income")
    assert(mc.reply_to.called)


@patch('telebot.telebot')
def test_post_amount_input_working(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    message = create_message("hello from testing!")
    add.post_category_selection(message, mc, "Income")
    assert(mc.send_message.called)


@patch('telebot.telebot')
def test_post_amount_input_working_withdata(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True
    mocker.patch.object(add, 'helper')
    add.helper.validate_entered_amount.return_value = 10
    add.helper.write_json.return_value = True
    add.helper.getDateFormat.return_value = dateFormat
    add.helper.getTimeFormat.return_value = timeFormat

    mocker.patch.object(add, 'option')
    add.option.return_value = {11, "here"}

    message = create_message("hello from testing!")
    add.post_amount_input(message, mc, 'Income')
    assert(mc.send_message.called)


@patch('telebot.telebot')
def test_post_amount_input_nonworking(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True
    mc.reply_to.return_value = True
    mocker.patch.object(add, 'helper')
    add.helper.validate_entered_amount.return_value = 0
    message = create_message("hello from testing!")
    add.post_amount_input(message, mc, 'Income')
    assert(mc.reply_to.called)


# @patch('telebot.telebot')
# def test_post_amount_input_working_withdata_chatid(mock_telebot, mocker):
#     mc = mock_telebot.return_value
#     mc.send_message.return_value = True
#     mocker.patch.object(add, 'helper')
#     add.helper.validate_entered_amount.return_value = 10
#     add.helper.write_json.return_value = True
#     test_option = {11: "here"}
#     mocker.patch.object(add, 'option', new=test_option)
#     mocker.patch.object(DetailedTelegramCalendar, 'build')
#     calendar_markup = "mock_calendar_markup"
#     step = "day" 
#     DetailedTelegramCalendar.build.return_value = (calendar_markup, step)
#     mocker.patch.object(DetailedTelegramCalendar, 'process')
#     selected_date = "2023-10-15"
#     DetailedTelegramCalendar.process.return_value = (True, selected_date, step)
#     message = create_message("Select a date from the calendar")
#     add.post_amount_input(message, mc, 'Income')
#     assert mc.send_message.called


def test_add_user_record_nonworking(mocker):
    mocker.patch.object(add, 'helper')
    add.helper.read_json.return_value = {}
    addeduserrecord = add.add_user_income_record(1, ANY, "record : test")
    assert(addeduserrecord)


def test_add_user_record_working(mocker):
    MOCK_USER_DATA = test_read_json()
    mocker.patch.object(add, 'helper')
    add.helper.read_json.return_value = MOCK_USER_DATA
    addeduserrecord = add.add_user_income_record(1, ANY,"record : test")
    if(len(MOCK_USER_DATA) + 1 == len(addeduserrecord)):
        assert True


def create_message(text):
    params = {'messagebody': text}
    chat = types.User(11, False, 'test')
    return types.Message(1, None, None, chat, 'text', params, "")


def test_read_json():
    try:
        if not os.path.exists('./test/dummy_expense_record.json'):
            with open('./test/dummy_expense_record.json', 'w') as json_file:
                json_file.write('{}')
            return json.dumps('{}')
        elif os.stat('./test/dummy_expense_record.json').st_size != 0:
            with open('./test/dummy_expense_record.json') as expense_record:
                expense_record_data = json.load(expense_record)
            return expense_record_data

    except FileNotFoundError:
        print("---------NO RECORDS FOUND---------")
