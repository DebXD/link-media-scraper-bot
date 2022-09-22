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
    script = soup.find("script", {"type":"application/json"})

    url_list = []
    for i in script:
        f = json.loads(i)
        #print(f)
        for key , items in f.items():
            if key == "props":
                item = items.get("pageProps")
                item2 = item.get("album")

                item3 = item2.get('files')
                #print(item3)
                length = len(item3)              
                for i in range(length):
                    name = item3[i].get('name')
                    cdn_url = item3[i].get('cdn')
                    cdn = cdn_url.strip("https://cdn.bunkr.is")
                    if cdn == "":
                        url = "https://media-files.bunkr.is/" + name
                        print(url)
                        url_list.append(url)
                    else:
                        url = f"https://media-files{cdn}.bunkr.is/" + name
                        print(url)
                        url_list.append(url)
                return url_list