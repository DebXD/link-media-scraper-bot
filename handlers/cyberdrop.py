import requests, os, time

import helpers.grabber
import utils.get_extension


session = requests.Session()

def exec_cyberdrop(client,message):
    
    text = message.text[11:]
    chat_id = message.chat.id
    msg_id = message.message_id
    print(text)
    
    if text == "":
        client.send_message(chat_id=chat_id, text="Enter a Cyberdrop Link")
    else:
        url_list = helpers.grabber.get_urls(text)
        print(url_list)
        client.send_message(chat_id=chat_id, text="Please Wait...")

        for link in url_list:
            extension = utils.get_extension.get_url_extension(link)
            print(extension)

            if extension == ".jpg":
                try:
                    response = session.get(link, allow_redirects= True)
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
                    print("Sending video...")
                    
                    
                    
                    
                    try:
                        import thumbnail.thumb
                    
                        thumbnail_path = thumbnail.thumb.make_thumbnail()
                        
                        
                        client.send_video(chat_id = chat_id, video = open("video.mp4","rb"), thumb=open(thumbnail_path,"rb"))
                        
                        os.remove(directory+"/"+ thumbnail_path)
                        
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