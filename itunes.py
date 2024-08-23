import requests

band_name = input('Name a band.\n')
response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + band_name)
print('5 songs from', band_name, 'are:\n')
o = response.json()

for result in o["results"]:
    if result["trackName"] == band_name:
        continue
    if result["trackName"] != band_name:
        print(result["trackName"])