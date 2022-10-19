# link-media-scraper-bot
A Telegram bot that used to download or upload the media contents from cyberdrop, bunkr and streamtape links.

## Simply Deploy on Heroku (Easier Way):

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/DebXD/link-media-scraper-bot)
## Supported Handlers and Features :
 * `/cyberdrop [link]` For cyberdrop links 
 * `/bunkr [link]` For bunkr links 
 * `/streamdl [link]` For streamtape leeching. see environment variable section before using this command
 *  Send any video to upload it to streamtape. see environment variable section...
 * `/ping` Check latency
 * `/help` To know about commands
 

 ## Deploy Locally :
 ### Termux:
 ```
 git clone https://github.com/DebXD/link-media-scraper-bot
 cd link-media-scraper-bot
 ```
 * Install the required libraries :
 ```
 pip3 install wheel
 apt install libxml2 libxslt wget ffmepg
 pip3 install -r requirements.txt
 ```
 * If Pillow Installation Fails on Termux Run this :
 ```
 apt install libjpeg-turbo
 LDFLAGS="-L/system/lib64/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install Pillow
```
### Linux :
```
 git clone https://github.com/DebXD/link-media-scraper-bot
 cd link-media-scraper-bot
 pip3 install -r requirements.txt
 ```
 ## Environmet Variables :
 
 * * API ID (Required) :
 Your Telegram account API_ID, Get it from [my.telegram.org](https://my.telegram.org)
 
 * * API HASH (Required) :
 Your Telegram account API_HASH, Get it from [my.telegram.org](https://my.telegram.org)
 
 * * BOT TOKEN (Required) :
 The Token of Your Bot, Get it from [BotFather](https://t.me/BotFather)
 
 * LOG CHAT ID (Optional) :
 Your CHAT_ID where you want to get bot run notification.
 
 * API USERNAME (Optional) :
 Your [streamtape](https://streamtape.com) API USERNAME from account panel to access the streamtape functionalities.
 
 * API PASSWORD (Optional) :
 Your [streamtape](https://streamtape.com) API PASSWORD from account panel to access the streamtape functionalities.
 
  * HTTP/HTTPS PROXY (Optional) :
 Your [PROXY](https://webshare.io/) Sign Up and get the retotaing proxy if bunkr command(handler) crashes.

 ### Usage: 
 - Paste these variable in `example.env` and rename it to `.env` afterwards. Do not add inverted comma or quotes.
 
 #### Run:
```
$ python3 bot.py
```
That's it.
* Feel free to report any issues you have faced.<br>
Thanks for Using.
_ _ _
