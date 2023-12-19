# a) Given the following dictionary:
# dict_to_jsonify = {'iron': 5, 'silver': 7, 'gold': 3, 'copper': 4}
# Write a program that produces indented json string from the dictionary.
import json

dict_to_jsonify = {'iron': 5, 'silver': 7, 'gold': 3, 'copper': 4}
formatted_json = json.dumps(dict_to_jsonify, indent = 2, sort_keys = True, separators = (", ", " = "))

print(formatted_json)

# b) Given the following json string:
# employee_json = '{"name": "Teppo", "age": 32, "class": "IT"}'
# Write a program that produces a python object from the string.

employee_json = '{"name": "Teppo", "age": 32, "class": "IT"}'
obj_from_json_str = json.loads(employee_json)

print(obj_from_json_str)