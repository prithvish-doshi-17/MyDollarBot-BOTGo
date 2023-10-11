import helper


def run(message, bot):
    chat_id = message.chat.id
    user_list = helper.read_json()
    print(user_list)
    if str(chat_id) in user_list:
        user_list[str(chat_id)]['budget']['overall'] = None
        user_list[str(chat_id)]['budget']['category'] = None
        helper.write_json(user_list)
    bot.send_message(chat_id, 'Budget deleted!')
