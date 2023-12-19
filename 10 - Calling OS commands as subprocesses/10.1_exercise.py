#1) Implement a Python script that completes the following steps:
#  - Create a random number (5-10) of new, empty randomly named files;
#  - Associate an index with each of these files in your script (that is a number from 1 to <the number of files you have>);
#  - Write the following string to each of the files:
#     This file's index is: <index>
#     Replace the <index> with the actual index of the file
#  - Read the contents of the files and print that on screen;
#  - Remove the files.
#*Be careful with the last step. Take a snapshot of your VM to be sure.
import random
import os

file_names = ["banana.txt", "test.txt", "document.txt", "test_doc.txt", "example.txt", "banana_log.txt"]
files_list = []

for num in range(random.randint(5,10)):
    files_list.append(str(num + 1) + "_" + random.choice(file_names))

# convert a file_names list to string:
parameters = " "
parameters = parameters.join(files_list)

os.system(f"touch {parameters}; ls -l")

for k in range(len(files_list)):
    if files_list[k][1] in "0123456789":
# append the indexes to each of the files:
        with open(files_list[k], 'a') as fh:
            fh.write(f"This file's index is: {files_list[k][0:2]}")
    else:
        with open(files_list[k], 'a') as fh:
            fh.write(f"This file's index is: {files_list[k][0]}")
# display the contents of the files:
    with open(files_list[k], 'r') as fh:
        print(fh.read())

# remove the files:
os.system(f"rm -i {parameters}")