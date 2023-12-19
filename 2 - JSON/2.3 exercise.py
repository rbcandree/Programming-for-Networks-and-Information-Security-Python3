# Acquire the JSON file from: https://jsonplaceholder.typicode.com/todos
# Implement a function that explores the form of the JSON file and outputs the following information:
# - The keys used in the dictionary;
# - The range of userIds;
# - The range of taskIds;
# - The number of completed tasks;
# - The number of tasks with the word "delectus" in their title.

import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos')

def explore_jsn(data):
        # Output the keys used in the dictionary
    keys_lst = []  
    for element in data[0:1]:
        for key in element.keys():  #== list(element.keys()
            keys_lst.append(key)
    keys_lst_str = ", ".join(str(element) for element in keys_lst)
    print(f"The keys used in the dictionary are: {keys_lst_str}.")

        # -The range of userIds
    userIds_lst = []
    for element in data:
        if element['userId'] not in userIds_lst:
            userIds_lst.append(element['userId'])
    # print(userIds_lst)
    range_userId_a = min(userIds_lst)
    range_userId_b = max(userIds_lst) + 1
    print(f"The range of userId's is: ({range_userId_a}, {range_userId_b}).")

        # -The range of taskIds
    taskId_lst = []
    for element in data:
        if element['id'] not in taskId_lst:
            taskId_lst.append(element['id'])
    #print(taskId_lst)
    range_taskId_a = min(taskId_lst)
    range_taskId_b = max(taskId_lst) + 1
    print(f"The range of taskId's is: ({range_taskId_a}, {range_taskId_b}).")

        # -The number of completed tasks
    counter = 0
    for element in data:
        if element['completed'] == True:
            counter += 1
    #print(counter)
    print(f"The number of completed tasks is: {counter}.")

        # -The number of tasks with the word "delectus" in their title
    delectus = 0
    for element in data:
        if 'delectus' in element['title']:
            delectus += 1
    #print(delectus)
    print(f"The number of tasks with the word 'delectus' in their title: {delectus}.")

data = response.json()
explore_jsn(data)