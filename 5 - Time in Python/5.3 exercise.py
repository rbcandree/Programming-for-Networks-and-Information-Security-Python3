#3  In weather-data.json roadstations with roadstation Id's 10038 and 19958 have faulty time synchronization.
#   Fix the timestamps of all the measurements done on these stations by adding 
#   2 minutes to the measuredtime attributes of the measurements and writing the corrected information 
#   into the weather-data.json overwriting the faulty information.
import json
from datetime import datetime,  timedelta

with open('D:\\path_to_the_file\\weather-data.json', 'r') as fh:
    data =json.load(fh)

for element in data['weatherStations']:
    if element['id'] == 10038 or element['id'] == 19958:
        date_obj = element['measuredTime']
        format_str = "%Y-%m-%dT%H:%M:%SZ"
        dt_obj = datetime.strptime(date_obj, format_str)
        dt_obj = dt_obj + timedelta(minutes = 2)
        element['measuredTime'] = dt_obj.strftime('%Y-%m-%dT%H:%M:%SZ')
    for element1 in element['sensorValues']:
        if element1['roadStationId'] == 10038 or element1['roadStationId'] == 19958:
            date_obj1 = element1['measuredTime']
            format_str = "%Y-%m-%dT%H:%M:%SZ"
            dt_obj1 = datetime.strptime(date_obj1, format_str)
            dt_obj1 = dt_obj1 + timedelta(minutes = 2)
            element1['measuredTime'] = dt_obj1.strftime('%Y-%m-%dT%H:%M:%SZ')
            continue

with open('D:\\path_to_the_file\\weather-data.json', 'r+') as fh:
    json.dump(data, fh, ensure_ascii = False, sort_keys = False, indent = 1)