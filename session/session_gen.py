from pyrogram import Client
from decouple import config

api_id = config("API_ID")
api_hash = config("API_HASH")
bot_token = config("BOT_TOKEN")

def gen_session():
    app = Client("my_bot",api_id,api_hash,bot_token=bot_token)
    with app:
        session_string = app.export_session_string()
        app = Client(session_string, api_id,api_hash,bot_token=bot_token)
        return app
