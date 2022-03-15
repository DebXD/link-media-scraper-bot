import requests, json, os
from decouple import config

login_id = config('API_USERNAME')
key_id = config('API_PASSWORD')
session = requests.Session()

def upload_video():
    cred = { "login":login_id,"key":key_id }
    print("Please be Patient")
    response = session.get("https://api.streamtape.com/file/ul?",headers=cred)
    
    data = json.loads(response.text)
    ul_url = data.get('result').get('url')


    #Enter Path to the file
    local_path = os.getcwd()
    path =local_path + "/downloads/video.mp4"

    print("Uploading...")
    files = { 'file' : ("@"+path,open(path,'rb'), 'multipart/form-data')}


    headers = { "login":login_id,"key":key_id }
    try:
        response = session.post(ul_url, files = files, headers=headers)
        data = json.loads(response.text)
        url = data.get('result').get('url')
        size_in_bytes = data.get('result').get('size')
        #mb = int(size_in_bytes)/1024/1024
        print("Uploaded Successfully")
        os.remove(path)
        print("video is cleaned")
        return url
    except Exception as e:
        print(e)