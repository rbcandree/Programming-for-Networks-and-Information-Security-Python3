# Take the JSON from the exercise #1. The related user information can be found from:
# https://jsonplaceholder.typicode.com/users
# Use these 2 JSON files and programmatically find out the names of the users with the most completed tasks. 
# You can assume that the id in the users -JSON refers to the userID in the todos JSON:
# https://jsonplaceholder.typicode.com/todos

import json
with open('D:\\path_to_the_file\\users.json') as fh:
    users_data =json.load(fh)
with open('D:\\path_to_the_file\\todos.json') as fh:
    todos_data =json.load(fh)

def todos_update (todos_data, users_data):
    for element_todos in todos_data:
        for element_users in users_data:
            if element_todos['userId'] == element_users['id']:
                element_todos.update(name = element_users['name'])
            else:
                continue
    #print(todos_data)

new_obj = {}
def users_efficiency (todos_data):
    for element_todos in todos_data:
        value = 1
        if element_todos['completed'] == True:
            try:
                new_obj[element_todos['name']] += value
            except KeyError:
                new_obj[element_todos['name']] = value
        else:
            continue
    #print(new_obj)

def best (new_obj):
    leaders = []
    for key in new_obj:
        if new_obj[key] == max(new_obj.values()):
            leaders.append(key)
    leaders_str = ", ".join(str(name) for name in leaders)

    #print(leaders)
    print(f"The names of the users with the most completed tasks are: {leaders_str}.")

todos_update(todos_data, users_data)
users_efficiency (todos_data)
best (new_obj)