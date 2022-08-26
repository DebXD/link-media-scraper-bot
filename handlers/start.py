def exec_welcome(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    client.send_message(chat_id = chat_id, text=f"Hi **{first_name}**!\nChat ID : `{chat_id}`")
