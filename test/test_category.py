import os
import json
import mock
from mock.mock import patch
from telebot import types
from main import category
from mock import ANY


dateFormat = '%d-%b-%Y'
timeFormat = '%H:%M'
monthFormat = '%b-%Y'


@patch('telebot.telebot')
def test_run(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.reply_to.return_value = True
    message = create_message("hello from test run!")
    category.run(message, mc)
    assert(mc.reply_to.called_with(ANY, 'Select Operation', ANY))

@patch('telebot.telebot')
def test_post_operation_selection_working(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    message = create_message("hello from testing!")
    category.post_operation_selection(message, mc)
    assert(mc.send_message.called)

@patch('telebot.telebot')
def test_post_operation_selection_noMatchingCategory(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    mocker.patch.object(category, 'helper')
    category.helper.getCategoryOptions.return_value = {}

    message = create_message("hello from test_category.py!")
    category.post_operation_selection(message, mc)
    mc.send_message.assert_called_with(11, 'Invalid', reply_markup=mock.ANY)

def create_message(text):
    params = {'messagebody': text}
    chat = types.User(11, False, 'test')
    return types.Message(1, None, None, chat, 'text', params, "")

