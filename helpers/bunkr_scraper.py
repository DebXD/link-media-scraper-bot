from bs4 import BeautifulSoup
from decouple import config
import asyncio
import aiohttp

http_proxy = config('HTTP_PROXY')
https_proxy = config('HTTPS_PROXY')

async def bunkr_scraper(url):

    async def get_text(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                return await res.text()


    async def res(url):
    
        html_content = await get_text(url)

        soup = BeautifulSoup(html_content, "html.parser")
        url_list = []
        for link in soup.find_all("a"):
            href = link.get("href") 
            if len(href) > 30:
                if "/v/" in href:
                    modified_href = "https://bunkr.su" + href
                    print(modified_href)
                    url_list.append(modified_href)
                else:
                    print(href)
                    url_list.append(href)
        return url_list
    url_list = asyncio.run(res(url))
    return url_list