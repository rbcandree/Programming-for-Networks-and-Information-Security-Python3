#1  Python module os contains operating system commands.
# a) Import the module and use os.getcwd to get the current working directory and print that on screen.
import os

current_working_directory = os.getcwd()
print(f"The current working directory is: {current_working_directory}")

# b) Afterward change the working directory with os.chdir("path_to_the_new_directory").
os.chdir('D:\\path_to_the_new_directory')
new_working_directory = os.getcwd()
print(f"The new working directory is: {new_working_directory}")

# c) Use os.listdir() to check the contents of your current working directory.
contents = os.listdir(new_working_directory)
print(contents)