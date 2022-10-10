# link-media-scraper-bot
A Telegram bot that used to download or upload the media contents from cyberdrop, bunkr and streamtape links.

## Simply Deploy on Heroku (Easier Way):

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/DebiprasadXD/link-media-scraper-bot)
## Supported Handlers and Features :
 * `/cyberdrop [link]` For cyberdrop links 
 * `/bunkr [link]` For bunkr links 
 * `/streamdl [link]` For streamtape downloading - 
 * `/ping` Fheck latency with 
 * Send any video to upload it to streamtape.

 ## Deploy Locally :
 ### Termux:
 ```
 git clone https://github.com/DebiprasadXD/link-media-scraper-bot
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
 git clone https://github.com/DebiprasadXD/link-media-scraper-bot
 cd link-media-scraper-bot
 pip3 install -r requirements.txt
 ```
 ## Environmet Variables :
 
 * * API ID (Required) :
 Your Telegram account API_ID, Get it from [my.telegram.org](https://my.telegram.org)
 
 * * API HASH (Required) :
 Your Telegram account API_HASH, Get it from [my.telegram.org](https://my.telegram.org)
 
 * * BOT TOKEN (Required) :
 Enter the Token of Your Bot, Get it from [BotFather](https://t.me/BotFather)
 
 * LOG CHAT ID (Optional) :
 Enter your CHAT_ID where you want to get bot run notification.
 
 * API USERNAME (Optional) :
 Enter Your [streamtape](https://streamtape.com) API USERNAME from account panel to access the streamtape functionalities.
 
 * API PASSWORD (Optional) :
 Enter Your [streamtape](https://streamtape.com) API PASSWORD from account panel to access the streamtape functionalities.
 
  * HTTP/HTTPS PROXY (Optional) :
 Enter Your [PROXY](https://webshare.io/) Sign Up and get the retotaing proxy if bunkr command(handler) crashes.

 ### Usage: 
 - Paste these variable in `example.env` and rename it to `.env` afterwards. Do not add inverted comma or quotes.
 
 #### Run:
```
$ python3 bot.py
```

That's it.
* Feel free to report any issues you have faced.
Arigato Gozaimasu(Thanks) ;)
_ _ _
