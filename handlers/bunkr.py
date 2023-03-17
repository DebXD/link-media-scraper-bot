import requests, os, time
import json

import helpers.bunkr_scraper
import utils.get_extension
import urllib3

session = requests.Session()

def exec_bunkr(client,message):
    text = message.text[7:]
    chat_id = message.chat.id
    msg_id = message.id
    print(text)
    
    if text == "":
        client.send_message(chat_id=chat_id, text="Enter a Bunkr Link")
    else:
        client.send_message(chat_id=chat_id, text="Please Wait...")
        print(text)
        r = session.get(text)

        if r.status_code == 403:
            print("***Use Proxy sir***")
            
            
        else:
            url_list = helpers.bunkr_scraper.bunkr_scraper(text)
           
        for url in url_list:
            extension = utils.get_extension.get_url_extension(url)
            #print(extension)
            print(f"Downloading...{extension}")
            response = session.get(url, allow_redirects= True, verify=False,)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            if response.status_code == 200:
                if extension == ".jpg":
                    try:
                        open("image.jpg","wb").write(response.content)
                        print(f"Uploading {extension}...")
                        

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
                        open("image.png","wb").write(response.content)
                        directory = os.getcwd()
                        print(f"Uploading {extension}...")

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
                        open("video.mp4","wb").write(response.content)
                        directory = os.getcwd()
                        
                        try:
                            import thumbnail.thumb
                        
                            thumbnail_path = thumbnail.thumb.make_thumbnail()


                            client.send_video(chat_id = chat_id, video = open("video.mp4","rb"), thumb=open(thumbnail_path,"rb"))

                            os.remove(directory+"/"+ thumbnail_path)
                            
                            print("Sent")
                            os.remove(directory+"/video.mp4")
                            print(f'{extension} removed.')
                            time.sleep(0.1)
                        except Exception as e:
                            print(e)
                    except Exception as e:
                        print(e)

        print("Task is Completed")
        client.send_message(chat_id = chat_id, text="Task Completed", reply_to_message_id = msg_id)
