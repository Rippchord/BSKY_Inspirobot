import requests
import cv2 

downloadURL = "http://inspirobot.me/api?generate=true"

req = requests.get(downloadURL)

filename = req.text[req.text.rfind('/')+1:]

def download_file(url, filename=''):
    try:
        if filename:
            pass
        else: 
            filename = req.url[req.url.rfind('/')+1:]

        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e: 
        print(e)
        return None
    
download_file(req.text, filename)

img = cv2.imread(filename, 2) 
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 


cv2.imshow("Binary", bw_img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

# https://generated.inspirobot.me/a/jDe2R4WGez.jpg

