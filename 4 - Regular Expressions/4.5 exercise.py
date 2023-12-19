# 5 We'll often end up in a situation where we want to run some regex pattern against a
# whole file and we want to process all the matches found. 
# This can be achieved by using findall() function from the re library:

# - our pattern in regex format
# pattern = r'some regex pattern'

# - create the file handling:
# fh = open('some_file.txt', 'r')

# - feed the file into re.findall(). 
# This results in a list of the matches.

# Notice here how fh.read() reads through the whole file.
# matches_as_list = re.findall(pattern, fh.read())

# Use this information to go through the good old weather-data.json to find all references
# to either "TIE" or "surfacemoisture". Print the number of these findings. 
# Note that the wanted references are case sensitive.
"""
import re
with open('D:\\path_to_the_file\\weather-data.json', 'r') as fh:
    matches_as_list = re.findall(r'(TIE|surfacemoisture)', fh.read())
    print(f"{len(matches_as_list)} hits for 'TIE', 'surfacemoisture' in the file.")
"""
# Would you be able to find the whole measurement data related to these findings?

import re

with open('D:\\path_to_the_file\\weather-data.json', 'r') as fh:
    matches_as_list = re.findall(r'(\"\w+\"\s\:\s\"\w+TIE\"|\"\w+\"\s\:\s\"TIE\w+\"|\"\w+\"\s\:\s\"surfacemoisture\w\")', fh.read())
    print(set(matches_as_list))

#"name" : "KASTEPISTE_ERO_TIE",     r'\"\w+\"\s\:\s\"\w+TIE\"'
#"name" : "TIE_2_DERIVAATTA",       r'\"\w+\"\s\:\s\"TIE\w+\"'
#"oldName" : "surfacemoisture1",    r'.+surfacemoisture.+'  -->  r'\"\w+\"\s\:\s\"surfacemoisture\w\"'