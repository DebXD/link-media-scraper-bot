import requests
from bs4 import BeautifulSoup
import json
from decouple import config

session = requests.Session()
http_proxy = config('HTTP_PROXY')
https_proxy = config('HTTPS_PROXY')

def bunkr_scraper(url):
    r = session.get(url,proxies={
            "http": http_proxy,
            "https": https_proxy })

    soup = BeautifulSoup(r.text,'html.parser')
    soup2 = soup.find_all("script")
    for i in soup2[11]:
        f = json.loads(i)
    
    
    for key , items in f.items():
        if key == "props":
            item = items.get("pageProps")
            item2 = item.get("files")
            length = len(item2)
    url_list = []
    for i in range(length):
        name = item2[i].get('name')
        url = "https://media-files.bunkr.is/" + name
        url_list.append(url)
    return url_list

