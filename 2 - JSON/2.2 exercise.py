# Implement a program that opens weather-data.json 
# You can open this file from your own hard drive like this:
# notice the use of the escape character \ in front of the directory path steps.

# import json
# with open('D:\\path_to_the_file\\weather-data.json') as fh:
#     data =json.load(fh)

# Find out programmatically how many KUITUVASTE_SUURI_1 measurements have been made. 
# You may need to have a look at the json file to find out how to handle it in Python.

import json
with open('D:\\path_to_the_file\\weather-data.json') as fh:
    data =json.load(fh)
    #formatted_data = json.dumps(data, indent = 2, separators = (", ", " = "))
counter = 0
for element in data['weatherStations']:
    for element1 in element['sensorValues']:
        if element1['name'] == 'KUITUVASTE_SUURI_1':
            counter += 1
            break

print(counter)
print("The KUITUVASTE_SUURI_1 measurements have been made: {} time(s)".format(counter))