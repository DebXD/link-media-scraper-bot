def exec_help(client, message):
    chat_id = message.chat.id
    msg_id = message.message_id
    client.send_message(chat_id =chat_id,text = "Supported Handlers: \n`/cyberdrop [link]` for cyberdrop links \n`/bunkr [link]` for bunkr links\n/`streamdl [link]` for streamtape to download",reply_to_message_id = msg_id)