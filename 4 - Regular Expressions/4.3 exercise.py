# 3
# a) Write down rules to form a working email address. 
#   There's no need to conform with all the specifics but your rule set should at least cover the most common cases, 
#   like first_name.last_name@gmail.com
# b) Form a regular expression that matches such strings that conform with the ruleset.
# c) Write a program that asks the user for an e-mail address, validates the given address and tells the user 
#   if the e-mail address conformed with the ruleset. Use regular expressions.
"""
a) E-mail address creating rules:
    - Starts with a username, which can consist characters as: a-z, A-Z, dot '.', -, _          ==  ^[a-zA-Z0-9._-]     [a-zA-Z0-9_] == \w
    - after username should always be conjunction <@> symbol:                                   ==  +@
    - <@> follows with a hostname in format <xxxxx.xxx>:
        1st part of a hostname can consist: a-z, A-Z, dot '.', -                                ==  [a-zA-Z0-9.-]
        2nd part of a hostname is a domain:
        starts specifically with a dot '.' and ends with 2-3 characters of a-z or A-Z:          ==  +\.[a-zA-z]{2,3}$
"""
import re
def email_valid (user_input):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,3}$'
    match = re.search(pattern, user_input)
    if match:
        print(f"Your e-mail address: {user_input} is valid.")
    else:
        print(f"Invalid e-mail address. Please, try again.")

check = email_valid(input("Enter your e-mail, please:"))