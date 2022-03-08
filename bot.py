from pyrogram import Client
from pyrogram import filters
import grabber
from decouple import config
import get_extension, get_link_id
import requests, os, time


session = requests.Session()

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
    
##--------------START---------------
@app.on_message(filters.command(["start","help"]))
def log(client, message):
    #print(message)
    
    text = message.text
    user_id = message.from_user.id
    chat_id = message.chat.id
    chat_type = message.chat.type
    first_name = message.from_user.first_name
    if chat_type == "private":
        client.send_message(chat_id =chat_id,text=f"Hi **{first_name}**\nChat Type : {chat_type}\nChat ID : `{chat_id}`" )
        
    else:
        client.send_message(chat_id = chat_id, text=f"Hi **{first_name}**\nChat Type : {chat_type}\nChat ID : `{chat_id}`")
##CYBERDROP-----------------##        
@app.on_message(filters.command("cyberdrop"))
def send_cybermedia(client,message):
    text = message.text[11:]
    chat_id = message.chat.id
    msg_id = message.message_id
    print(text)
    if text == "":
        client.send_message(chat_id=chat_id, text="Enter a Cyberdrop Link")
    else:
        url_list = grabber.get_urls(text)
        print(url_list)
           
        for link in url_list:    
            extension = get_extension.get_url_extension(link)
            print(extension)
            
            if extension == ".jpg":
                try:
                    response = session.get(link, allow_redirects= True)
                    open("image.jpg","wb").write(response.content)
                    directory = os.getcwd()
                    print("Sending image...")
                    
                    try:
                        client.send_photo(chat_id = chat_id, photo = open("image.jpg","rb"))
                        print("Sent")
                        
                        time.sleep(0.1)
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)
            elif extension == ".png":
                try:
                    response = session.get(link, allow_redirects= True)
                    open("image.png","wb").write(response.content)
                    directory = os.getcwd()
                    print("Sending image...")
                    
                    try:
                        client.send_photo(chat_id = chat_id, photo = open("image.png","rb"))
                        print("Sent")
                        
                        time.sleep(0.1)
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)
                    
                
            else:
                
                try:
                    print("Downloading...")
                    response = session.get(link, allow_redirects= True)
                    open("video.mp4","wb").write(response.content)
                    directory = os.getcwd()
                    print(directory)
                    print("Sending video...")
                    try:
                        client.send_video(chat_id = chat_id, video = open("video.mp4","rb"))
                        print("Sent")
                        os.remove(directory+"/video.mp4")
                        print('Video is Cleaned.')
                        time.sleep(0.1)
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)

        print("Task is Completed")
        client.send_message(chat_id = chat_id, text="Task Completed", reply_to_message_id = msg_id)
    
##---------BUNKR----------------##   
@app.on_message(filters.command("bunkr"))
def send_bunkrmedia(client,message):
    text = message.text[7:]
    chat_id = message.chat.id
    msg_id = message.message_id
    print(text)
    if text == "":
        client.send_message(chat_id=chat_id, text="Enter a Bunkr Link")
    else:
        url_list = grabber.get_urls(text)
        print(url_list)
           
        for link in url_list:    
            extension = get_extension.get_url_extension(link)
            print(extension)
            
            if extension == ".jpg":
                try:
                    response = session.get(link, allow_redirects= True)
                    open("image.jpg","wb").write(response.content)
                    directory = os.getcwd()
                    print("Sending image...")
                    
                    try:
                        client.send_photo(chat_id = chat_id, photo = open("image.jpg","rb"))
                        print("Sent")
                        
                        time.sleep(0.1)
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)
              
              
            elif extension == ".png":
                try:
                    response = session.get(link, allow_redirects= True)
                    open("image.png","wb").write(response.content)
                    directory = os.getcwd()
                    print("Sending image...")
                    
                    try:
                        client.send_photo(chat_id = chat_id, photo = open("image.png","rb"))
                        print("Sent")
                        
                        time.sleep(0.1)
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)
               
    
            else:
                link_id = get_link_id.get_link_id(link)
                resource_link = "https://media-files.bunkr.is/" + link_id
                print(resource_link)
                try:
                    print("Downloading...")
                    response = session.get(resource_link, allow_redirects= True)
                    open("video.mp4","wb").write(response.content)
                    directory = os.getcwd()
                    print(directory)
                    print("Sending video...")
                    try:
                        client.send_video(chat_id = chat_id, video = open("video.mp4","rb"))
                        print("Sent")
                        os.remove(directory+"/video.mp4")
                        print('Video is Cleaned.')
                        time.sleep(0.1)
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)
                    
        print("Task is Completed")
        client.send_message(chat_id = chat_id, text="Task Completed", reply_to_message_id = msg_id)
        
    
    
    
app.run()