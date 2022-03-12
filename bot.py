from pyrogram import Client
from pyrogram import filters
from decouple import config

from decouple import config

import handlers.cyberdrop
import handlers.bunkr
import handlers.start
import handlers.help
import handlers.streamdl
import handlers.streamul



api_id = config("API_ID")
api_hash = config("API_HASH")
bot_token = config("BOT_TOKEN")
log_chat_id = config("LOG_CHAT_ID")

app = Client("my_bot",api_id,api_hash,bot_token=bot_token)
with app:
    if log_chat_id != "None":
        app.send_message(chat_id=log_chat_id,text="I'm Running...")
    else:
        pass
    
##--------------START---------------##
@app.on_message(filters.command("start"))
def welcome(client, message):
    handlers.start.exec_welcome(client, message)
    
##--------------help---------------##
@app.on_message(filters.command("help"))
def send_help(client, message):
    handlers.help.exec_help(client,message)
    
##----------CYBERDROP--------------## 
@app.on_message(filters.command("cyberdrop"))
def send_cybermedia(client, message):
    handlers.cyberdrop.exec_cyberdrop(client, message)
    
##------------BUNKR----------------##   
@app.on_message(filters.command("bunkr"))
def send_bunkrmedia(client, message):
    handlers.bunkr.exec_bunkr(client, message)
    
    
##------------streamtape---Download----##
@app.on_message(filters.command("streamdl"))
def send_streamtape(client, message):
    if config("API_USERNAME") == "None" or config("API_PASSWORD") == "None":
        pass
    else:
        handlers.streamdl.exec_streamtapedl(client, message)
    
##-----------Streamtape---Upload------##
@app.on_message(filters.video)
def upload_streamtape(client,message):
    if config("API_USERNAME") == "None" or config("API_PASSWORD") == "None":
        pass
    else:
        
        handlers.streamul.exec_streamtapeul(client, message)
    
        
   
        
        
    
    
    
app.run()