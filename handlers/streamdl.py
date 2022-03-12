import helpers.streamtape_d
import os


def exec_streamtapedl(client, message):
 
    text = message.text[10:]
    print(text)
    msg_id = message.message_id
    chat_id = message.chat.id
    if text == "":
        client.send_message(chat_id=chat_id, text="Enter a Streamtape Link")
    else:
        helpers.streamtape_d.streamtape_dl(text)
        print("Uploading...")
        client.send_video(chat_id=chat_id, video = open("video.mp4","rb"))
        print("Sent")
        directory = os.getcwd()
        os.remove(directory + "/video.mp4")
