#   Exercise problem
#   Request the JSON–formatted user list from https://jsonplaceholder.typicode.com/users 
#   and form a new JSON that contains a list of the users with the following information only: 
#   name, phone number and geo location.

#   To make sure that you have formed the JSON correctly print the string 
import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/users')
data = response.json()

new_json = []

for element in data:
    new_obj = {}
    new_obj['name'] = element['name']
    new_obj['phone'] = element['phone']
    new_obj['geo'] = element['address']['geo']
    new_json.append(new_obj)

json_modified = json.dumps(new_json)
print(json_modified)