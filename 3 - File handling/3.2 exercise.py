#2 Reading CSV files
#   A CSV file (short for comma-separated values), is a text file which contains data separated 
# by a predetermined character. The most common characters used for this purpose are the comma , and the semicolon ;, 
# but any character is, in principle, possible.
#   CSV files are commonly used to store records of different kinds. Many database and spreadsheet programs, such as Excel, 
# can import and export data in CSV format, which makes data exchange between different systems easy.
#   We already learnt we can go through the lines in a file with a for loop, but how can we separate the different fields on a single line? 
# Python has a string method split for just this purpose. The method takes the separator character(s) as a string argument, and returns 
# the contents of the target string as a list of strings, separated at the separator.
#   Let's assume we have a file grades.csv, which contains names of students and the grades they received on some courses. 
# Each line has the data of a single student, and the data is separated by a semicolon.
#   Content of the grades.csv:
# Paul;5;4;5;3;4;5;5;4;2;4
# Beth;3;4;2;4;4;2;3;1;3;3
# Ruth;4;5;5;4;5;5;4;5;4;4

#preview = open('grades.csv', 'r')
#for element in preview:
#    print(element)

with open('grades.csv') as new_file:    # we are open grades.csv with file handling as new_file
                                        # combination of with and open():
                                        # unlike open() where we have to close the file with the close() method, 
                                        # the with statement closes the file for us without us telling it to. 
    for line in new_file:               # ... going through the lines in a new_file with a for loop
        line = line.replace('\n', '')   # replace() method replaces a specified phrase with another specified phrase.
                                        # string.replace(oldvalue, newvalue)
                                        # \n (new line)  will be replaced with an empty space (whitespace)
        parts = line.split(";")         # splits a string into a list where each word is a list item: string.split("separator")
                                        # .split() method takes the separator character(in our case: ';') as a string argument, 
                                        # and returns the contents of the target string as a list of strings, separated at ';'.
                                        # we can specify the separator, default separator is any whitespace.
        name = parts[0]                 # takes 1st item from the parts-list as a name-variable
        grades = parts[1:]              # takes from 2nd up to the last item from the parts-list as a grades-variable
        print(line)                     # shows lines before changes in the new_file
        print("Name:", name)
        print('Grades:', grades)

# Why is the replace() used here, why is it important? 
# Note that there's another string method in Python that can also be used for this kind of tasks called strip(). 
# Familiarize yourself with strip(), what are the main differences to replace()?

# The str.replace("old", "new") method is used to replace the substring old with the string new. 
# This method returns a new copy of the string with the replacement. The original string str is unchanged.

# The str.strip("parameter") method will return a copy of the string; will delete any character at the beginning or end of the string 
# that matches "any" character in the parameter we put in the strip function. 
# If no arguments are given the default is to strip whitespace characters.