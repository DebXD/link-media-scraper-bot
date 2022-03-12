def exec_welcome(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    chat_type = message.chat.type
    first_name = message.from_user.first_name
    if chat_type == "private":
        client.send_message(chat_id =chat_id,text=f"Hi **{first_name}** Thanks for starting me ;)\nChat Type : {chat_type}\nYour User ID : `{user_id}`" )

    else:
        client.send_message(chat_id = chat_id, text=f"Hi **{first_name}**\nChat Type : {chat_type}\nChat ID : `{chat_id}`")