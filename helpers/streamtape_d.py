import requests, json, time
from decouple import config
import utils.get_file_id
#import handlers.streamdl

#get_file_id = utils.get_file_id
def streamtape_dl(link):
    file_id = utils.get_file_id.get_file_id(link)
    print("Processing...")

    login_key = config('API_USERNAME')
    key = config('API_PASSWORD')

    headers = {'file':file_id,'login':login_key,'key':key}
    response = requests.get("https://api.streamtape.com/file/dlticket?",headers)
    data = json.loads(response.text)

    ticket = data.get('result').get('ticket')

    for i in range(3,0,-1):
        print(f"Please wait for {i} sec...")
        time.sleep(1)
        #without this sleep method api will return  error 403[forbidden]
    headers = {'file':file_id,'ticket':ticket,'login':login_key,'key':key}
    response = requests.get("https://api.streamtape.com/file/dl?",headers)
    data = json.loads(response.text)
    link = data.get('result').get('url')
    byte_size = data.get('result').get('size')
    size_in_MB = int(byte_size/1024/1024)
    print(f'File Size : {size_in_MB}MB')
    
    print("Downloading...")
    r = requests.get(link)
    open('video.mp4', 'wb').write(r.content)
    print("Download is Completed")
