from bs4 import BeautifulSoup
import asyncio
import aiohttp
from utils import get_extension


def bunkr_scraper(url):

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
                    html_text = await get_text(modified_href)
                    sp = BeautifulSoup(html_text, "html.parser")
                    for source in sp.find_all('source'):
                        link = source.get("src")
                        print(link)
                        url_list.append(link)
                else:
                    print(href)
                    extension = get_extension.get_url_extension(href)
                    image_extension_list = ['.jpg', '.png',".jpeg",".webp",".gif",".svg",".ico",".raw" ]
                    if  extension in image_extension_list:
                        url_list.append(href)
                    else:
                        html_text = await get_text(href)
                        sp = BeautifulSoup(html_text, "html.parser")
                        for source in sp.find_all('source'):
                            link = source.get("src")
                            print(link)
                            url_list.append(link)
        return url_list
    url_list = asyncio.run(res(url))
    return url_list