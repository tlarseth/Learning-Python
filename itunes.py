import json
import requests
import sys

user_band = input('Name a Band, and I will list 5 songs of theirs:  \n')
print()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + user_band)
print ('5 songs from your band are:  \n')
band_song = response.json()
for result in band_song["results"]:
    print(result["trackName"])