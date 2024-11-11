import os

from dotenv import load_dotenv, dotenv_values
from atproto import Client


import requests


import datetime as dt
import pytz
import time


load_dotenv()



tz = pytz.timezone('America/New_York')


dt_utcnow = dt.datetime.now()

dt_east = tz.localize(dt_utcnow)



def BSkeet(img):

    client = Client()
    client.login(os.getenv('BOT_USERNAME'), os.getenv('PASSWORD'))
    print('It worked!')
    with open(img, 'rb') as r: 
        client.send_image(text=dt_east.strftime('%a %d %b'), image= r, image_alt="randomly generated inspirational meme")







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




while True:
    dt_utcnow = dt.datetime.now()

    dt_east = tz.localize(dt_utcnow)

    if str(dt_east.strftime('%H:%M')) == '12:00':
        main()
        time.sleep(60)
        


