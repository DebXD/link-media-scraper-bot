import requests, json, time
from decouple import config
import utils.get_file_id
import helpers.get_dl_ticket
import helpers.get_dl_url

def streamtape_dl(link):
    file_id = utils.get_file_id.get_file_id(link)
    print("Processing...")
    print(file_id)

    login_key = config('API_USERNAME')
    key = config('API_PASSWORD')
    
    result = helpers.get_dl_ticket.get_ticket(file_id)
    print(result)
    if result is None:
        print("Result is None, Could not generate Ticket")
        return False
    else:
        ticket = result.get('ticket')
        print(ticket)
        print("Please wait for 5 sec...")
        time.sleep(5)
        #without this sleep method api will return  error 403[forbidden]
        link = helpers.get_dl_url.dl_url(ticket,file_id)
        print("Downloading...")
        try:
            r = requests.get(link)
            open('video.mp4', 'wb').write(r.content)
            print("Download is Completed")
        except Exception as e:
            print(e)
        return True
