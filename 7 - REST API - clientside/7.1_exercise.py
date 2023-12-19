"""
Use the following code as a basis for your Python script and print on screen the instructions for travelling from Tampere to Helsinki, 
the total travel time and travel distance. You can use the given apikey. Just make sure you don't spam the API with requests.
"""

# Your code begins from here. Check what the json_data holds and parse from there into more human readable form.

import requests
import urllib.parse
import json

api_key = "your_api_key"
url = "http://www.mapquestapi.com/directions/v2/route"

orig = "Tampere"
destination = "Helsinki"

url = url + "?" + urllib.parse.urlencode({"key":api_key,"from":orig,"to":destination})
print("Request URL:", url)
data = requests.get(url)
json_data = data.json()

#print(json.dumps(json_data, indent=4))

print("Total travel time:", json_data["route"]["formattedTime"])
print("Travel distance:", "{:.1f}".format((json_data["route"]["distance"])*1.6093), "km")

for way in json_data["route"]["legs"][0]["maneuvers"][0:-1]:  
    print(way["narrative"][:-15], "Go for", "{:.1f}".format((way["distance"])*1.6093), "km")
updates = len(json_data["route"]["legs"][0]["maneuvers"])
print(json_data["route"]["legs"][0]["maneuvers"][updates-1]["narrative"])