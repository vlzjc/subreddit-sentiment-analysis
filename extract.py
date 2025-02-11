import requests
import json

url = "https://reddit-scraper2.p.rapidapi.com/sub_posts"

querystring = {"sub":"Showerthoughts","sort":"TOP","time":"ALL"}

headers = {
    "x-rapidapi-key": "your key", #changed for my security and yours ;)
    "x-rapidapi-host": "reddit-scraper2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Save the JSON response to a file
with open('showerthoughts_posts.json', 'w') as json_file:
    json.dump(response.json(), json_file, indent=4)

print("JSON data saved to showerthoughts_posts.json")