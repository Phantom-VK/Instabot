import requests
import random
import tkinter as tk


#Imposrtant links
url = "https://api.pexels.com/v1/curated"
headers = {"Authorization": "wl80YOohp4aeCMdLTwlt2iFushjwq4biU42LT4tXPBVHoWLyO4Og0eBk"}

#Getting Response
response = requests.get(url, headers= headers).json()

#Generating Random number to pick a random image
already_picked_num = []
num = None
for number in num:
    if number in already_picked_num:
        num = random.randrange(1, 15)
        already_picked_num.append(num)





photo_id = response['photos'][num]["id"]
photo_url = response['photos'][num]["src"]["large"]
photographer = response['photos'][num]["photographer"]

print(f"Photo id : {photo_id}\nPhoto link: {photo_url}\nClicked by : {photographer}")

