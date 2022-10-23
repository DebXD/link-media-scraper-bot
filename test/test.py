from pyrogram import Client
from pyrogram import filters

from decouple import config

from pyrogram import Client
from pyrogram import filters

from decouple import config

import sys
sys.path.append('../')
import session.session_gen
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
