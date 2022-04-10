def exec_help(client, message):
    chat_id = message.chat.id
    msg_id = message.message_id
    client.send_message(chat_id =chat_id,text = "Supported Handlers: \n1. `/cyberdrop [link]` for cyberdrop links \n2. `/bunkr [link]` for bunkr links\n3. `/streamdl [link]` for streamtape to download\n4. Forward or Upload any video I'll Upload it to streamtape\n5.`/ping` to test latency between server and bot ",reply_to_message_id = msg_id)