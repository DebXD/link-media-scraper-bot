import session.session_gen
import handlers.cyberdrop
import handlers.bunkr
import handlers.start
import handlers.help
import handlers.streamdl
import handlers.streamul
import handlers.ping

log_chat_id = config("LOG_CHAT_ID")

app = session.session_gen.gen_session()
if app is not False:
    print('Bot is Running...')
    print('Test Successful')
with app:
    if log_chat_id != "None":
        app.send_message(int(log_chat_id),"Github Workflow ran successfully")
    else:
        pass
