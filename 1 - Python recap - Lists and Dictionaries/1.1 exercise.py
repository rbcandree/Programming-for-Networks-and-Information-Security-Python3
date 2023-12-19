"""
Implement a function such that given a list of strings as a parameter.
It counts the number of strings with the following requirements and RETURNS that number.
- The string has 2 or more characters. For example: 'ab', '12345', 'aaaa' BUT NOT ' ' or 'a');
- First and last character of the string are the same character. For example: 'aura', '1uiui1' BUT NOT 'abcd' or 'aaa '.
    
    An example:
Input:
[“tsirptsirp”, ”catnip-c”, ”regular”, ”something”]
Expected output (or rather, return value of the function):
2
"""
import random

def finder(lst):
    counter = 0
    for string in lst:
        #if (string[0] == string[len(string)-1]) and (len(string) >=2)
        if (string[0] == string[-1]) and (len(string) >=2):
            counter += 1
        else:
            continue
    return counter

characters = "abccdef -123"
string1 = ""
string2 = ""
string3 = ""
string4 = ""
string5 = ""
#how to implement part of code string1...5 with for loop?
for i in range(random.randint(1,10)):
    string1 += random.choice(characters)
for i in range(random.randint(1,10)):
    string2 += random.choice(characters)
for i in range(random.randint(1,10)):
    string3 += random.choice(characters)
for i in range(random.randint(1,10)):
    string4 += random.choice(characters)
for i in range(random.randint(1,10)):
    string5 += random.choice(characters)
    
lst = [string1, string2, string3, string4, string5]

print ("List:", lst)
print("Nuber of acceptable strings:", finder(lst))