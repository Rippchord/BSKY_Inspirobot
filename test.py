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



def BSkeet(func):
    def wrapper():
        client = Client()
        client.login(os.getenv('BOT_USERNAME'), os.getenv('PASSWORD'))
        with open(wrapper(), 'rb') as r: 
            client.send_image(text=dt_east.strftime('%a %d %b'), image= r, image_alt="randomly generated inspirational meme")
    return wrapper







@BSkeet
def download_file():
    if filename:
        pass
    else: 
        filename = 'temp'

    def wrapper():
        with requests.get(generateInspo()) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk) 
            return wrapper
        return filename

    

def generateInspo():
    downloadURL = "http://inspirobot.me/api?generate=true"
    req = requests.get(downloadURL)
    return req.text
    

def main():
    download_file()

main()
# generateInspo()



# while True:
#     dt_utcnow = dt.datetime.now()

#     dt_east = tz.localize(dt_utcnow)

#     if str(dt_east.strftime('%H:%M')) == '12:00':
#         print('It\'s time!')
#         time.sleep(60)
        
    # ==  dt.time(22,47,00):
    #     print("It's time")



