from main import budget_delete
from mock.mock import patch
from telebot import types


@patch('telebot.telebot')
def test_run_normal_case(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    mocker.patch.object(budget_delete, 'helper')
    budget_delete.helper.read_json.return_value = {'11': {'budget': {'budget': 10, 'category': 100}}}
    budget_delete.helper.write_json.return_value = True

    message = create_message("hello from testing")
    budget_delete.run(message, mc)

    # assert(mc.reply_to.called)
    mc.send_message.assert_called_with(11, 'Budget deleted!')


def create_message(text):
    params = {'messagebody': text}
    chat = types.User(11, False, 'test')
    message = types.Message(1, None, None, chat, 'text', params, "")
    message.text = text
    return message
