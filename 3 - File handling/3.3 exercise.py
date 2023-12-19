#3  Given a CSV file named "fruits.csv" with the following format:
# banana;6.50
# apple;4.95
# orange;8.0
# ...etc...

# Implement a function named read_fruits, which reads the file and returns a dictionary based on the content. 
# In the dictionary, use the name of the fruit as the key and the price as the value. 
# Serialize this dictionary into a JSON file called fruits.json. Make sure fruits.json is written on disk.
import json
import os

filename = "fruits.csv"
fruits = {}

def read_fruits(filename):
    with open(filename, 'r') as csvfile:
        for line in csvfile:
            line = line.replace('\n', '')
            parts = line.split(";")
            fruits[parts[0]] = float(parts[1])
        return fruits

def dict_to_json (fruits):
    with open('fruits.json', 'w') as fp:
        json.dump(fruits, fp)
    contents = os.listdir(os.getcwd())
    print(contents)

print(read_fruits(filename))
dict_to_json(fruits)