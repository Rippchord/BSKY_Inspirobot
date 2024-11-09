import requests
import json

response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    print(f"\n{data['title']}" + "\n" + f"{data['link']}\n", sep='\n \n')
