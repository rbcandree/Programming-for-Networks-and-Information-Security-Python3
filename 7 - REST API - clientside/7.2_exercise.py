"""
Here we will practice grabbing an access token for an API and using that token to authenticate a search request. 
Our aim here is just to get a list of available blobs from the API. You won't need to access the blobs.

We will be using the Machine-to-Machine approach.
a) To begin, we need to acquire an access token. For this we need to make a HTTP POST request to the API. This can be achieved by the post() -function of requests module as follows:

import requests
api_url = "https://example.com"
# Notice that you need to add the credentials to your request_data
request_data = {'key_1': 'value_1'}
response = requests.post(api_url, data = request_data)
print(response.json())

b) Store the token that the API returns in a variable to be used in the next step. 
Notice how response.json() is a dictionary type variable. We can access it like normal.

c) Send a HTTPS GET request to the API's search route with search type: blobs. 
Don't add any query parameters, so the API will reply with everything accessible to you. Add your access token to the request headers. 
Headers can be added as follows:

search_headers = {'key_1': 'value_1'}
search_url = "https://some_url.com"
search_response = requests.get(search_url, headers=sesarch_headers)

Credentials:
Username: your_username
Password: your_password
"""
import requests
import json
from operator import itemgetter

# a)
api_url = "https://your_api_url"
# Notice that you need to add the credentials to your request_data
uname = "your_username"
passwd = "your_password"
request_data = {'username': uname, 'password': passwd}
response = requests.post(api_url, data = request_data)
access_tkn = response.json()

# b)
tkn = access_tkn['access_token']
#print(tkn)

# c)
search_headers = {'token': tkn}
search_url = "https://your_api_url/data/search/blobs"
search_response = requests.get(search_url, headers=search_headers)
data = search_response.json()

#print(search_response)
print("From :", data["link"])
data["blobs"] = sorted(data["blobs"], key=itemgetter(0))
for file in data["blobs"]:
    print(file[0], file[1])