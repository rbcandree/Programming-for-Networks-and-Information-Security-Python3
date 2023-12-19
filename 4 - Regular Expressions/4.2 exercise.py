# 2  Implement a function that takes user input as argument and checks if the string 
# given by the user matches the following pattern. If a match is found, the function
# returns True. Otherwise it returns False. 
# Use regular expressions to check for the match.

# Patterns:
# a) The string only contains alphanumeric characters: meaning alphabet letters (a-z), (A-Z), numbers (0-9) and '_'
#    Characters: (space)!#%&? and dot '.'are not alphanumeric.
# b) The first three characters of the string are vowels.
# c) The string is a number greater than 100

# In the following the string between < >'s is the user input. <>'s are not part of the expected output.
"""
Expected output for a):
Give me a string: <"abcd123">
We found a match: True

Expected output for b):
Give me a string: <"aabbcc">
We found a match: False

Expected output for c):
Give me a string: <"123000111">
We found a match: True
"""
import re

def matches_pattern(user_input):
    print(f"Checking if, '{user_input}', matches the pattern.")
#    pattern = r'^[a-zA-Z0-9_]*$'            #  == r'^\w*$'                     The string only contains alphanumeric characters.
    pattern = r'^[aeiou]{3}\w*$'      #  == r'^[aeiou][aeiou][aeiou]'    The first three characters of the string are vowels.
#    pattern = r'^\d*$'                       #                                  The string is a number greater than 100.
#    match = re.search(pattern, user_input)
    match = re.search(pattern, user_input, re.IGNORECASE)   #   for b)
    if match:
        return True     #   for a) and b)
        #if int(match.group()) >= 100:
        #    return True
        #else:
        #    return False
    else:
        return False

did_it_match = matches_pattern(input("Give me a string: " ))
print("We found a match: ", did_it_match)