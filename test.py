import os

from dotenv import load_dotenv, dotenv_values
from atproto import Client


import requests
import inspirobot

import datetime as dt
import pytz
import time


load_dotenv()



tz = pytz.timezone('America/New_York')


def BSkeet(img):

    client = Client()
    client.login(os.getenv('BOT_USERNAME'), os.getenv('PASSWORD'))
    try: 
        with open(img, 'rb') as r: 
            client.send_image(text=dt_east.strftime('%a %d %b'), image= r, image_alt="randomly generated inspirational meme")
        with open('log.txt','a') as a:
            a.write("\n" + dt_east.strftime('%a %d %b: %H:%M:%S') + ': Success!')
    except Exception as e:
        with open('log.txt','a') as a:
            a.write("\n" + f"{dt_east.strftime('%a %d %b: %H:%M:%S')}: Error - {e}, {e.args}")










def download_file(func):
    image = func()
    with requests.get(image) as req:
        with open('temp.jpg', 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk) 
        return f

    

def generateInspo():
    downloadURL = "http://inspirobot.me/api?generate=true"
    req = requests.get(downloadURL)
    return req.text
    

def main():
    download_file(generateInspo)
    BSkeet('temp.jpg')



print('Waiting')

logtime_utcnow = dt.datetime.now()

lt_east = tz.localize(logtime_utcnow)

with open('log.txt','a') as a:
            a.write("\n" + lt_east.strftime('%a %d %b: %H:%M:%S') + ': Started!')

while True:
    dt_utcnow = dt.datetime.now()

    dt_east = tz.localize(dt_utcnow)

    if str(dt_east.strftime('%H:%M')) == '12:00':
        main()
        time.sleep(60)


        


