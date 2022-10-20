import requests ,json, time
from decouple import config

login_key = config('API_USERNAME')
key = config('API_PASSWORD')

def dl_url(ticket,file_id):
    #print(ticket, file_id)
    
    headers = {'file':file_id,'ticket':ticket,'login':login_key,'key':key}
    response = requests.get("https://api.strtape.tech/file/dl?",headers)
    data = json.loads(response.text)
    result = data.get('result')
    #print(result)
    if result is not None:
        link = result.get('url')
        #byte_size = data.get('result').get('size')
        #size_in_MB = int(byte_size/1024/1024)
        #print(f'File Size : {size_in_MB}MB')
        return link
    else:
        return "Not Found"
    