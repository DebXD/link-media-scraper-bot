import requests, os, time
import json

import helpers.bunkr_scraper
import utils.get_extension

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
            print("Use Proxy sir")
            
            
        else:
            url_list = helpers.bunkr_scraper.bunkr_scraper(text)
           
        for url in url_list:
            extension = utils.get_extension.get_url_extension(url)
            print(extension)

            if extension == ".jpg":
                try:
                    response = session.get(url, allow_redirects= True)
                    open("image.jpg","wb").write(response.content)
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
                    response = session.get(url, allow_redirects= True)
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
                    print("Downloading...vid")
                    response = session.get(url, allow_redirects= True)
                    open("video.mp4","wb").write(response.content)
                    directory = os.getcwd()
                    print("Sending video...")
                    try:
                        import thumbnail.thumb
                    
                        thumbnail_path = thumbnail.thumb.make_thumbnail()


                        client.send_video(chat_id = chat_id, video = open("video.mp4","rb"), thumb=open(thumbnail_path,"rb"))

                        os.remove(directory+"/"+ thumbnail_path)
                        
                        print("Sent")
                        os.remove(directory+"/video.mp4")
                        print('vid removed.')
                        time.sleep(0.1)
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)

        print("Task is Completed")
        client.send_message(chat_id = chat_id, text="Task Completed", reply_to_message_id = msg_id)
