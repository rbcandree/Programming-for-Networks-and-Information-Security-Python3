# Write a program that requests AIS (Automatic Identification System for marine vessels) metadata information from: 
# https://meri.digitraffic.fi/api/ais/v1/vessels 
# for a marine vessel identified by MMSI given as a command line argument to the script.
#
# Example input:
# python3 exercise_2.py 231319000
#
# Expected output:
# AIS metadata information for vessel identified by MMSI: 231319000
#{
#  "timestamp" : 1575510567036,
#  "destination" : "SURVEY",
#  "name" : "CECILIA",
#  "shipType" : 90,
#  "mmsi" : 231319000,
#  "callSign" : "OZ2157",
#  "imo" : 7381635,
#  "draught" : 43,
#  "eta" : 792832,
#  "posType" : 1,
#  "referencePointA" : 22,
#  "referencePointB" : 39,
#  "referencePointC" : 8,
#  "referencePointD" : 4
#}
import requests
import json
import argparse

response = requests.get('https://meri.digitraffic.fi/api/ais/v1/vessels')
data = response.json()

parser = argparse.ArgumentParser(description='Request the AIS metadata information for a marine vessel identified by MMSI')

# positional command line argument
parser.add_argument("mmsi", type=int, help="Identify the vessel by MMSI")
args = parser.parse_args()
vessel_mmsi = args.mmsi

for element in data:
    if vessel_mmsi == element['mmsi']:
        print(f"AIS metadata information for vessel identified by MMSI: {vessel_mmsi}")
        print(json.dumps(element, sort_keys = False, indent = 1))
    else:
        continue