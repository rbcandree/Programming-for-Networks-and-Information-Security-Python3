#4  Write a program which works as a simple diary. The diary entries should be saved in a file called diary.txt. 
#   When the program is executed, it should first read any and all entries already in the file. 
#   Then request a new entry from the user and store that in diary.txt.
#   ---
#   The expected output of the program on first run with the text in <>'s requested as input from the user:

#   Earlier entries:

#   New diary entry: <I did not sleep much today.>

#   Diary saved

#   The expected output of the second run of the same program with the text in <>'s requested as input from the user:

#   Earlier entries:

#   I did not sleep much today.

#   New diary entry: <Today was considerably better.>

#   Diary saved
#   ---
import os
import os.path

current_working_directory = os.getcwd()
path = f'{current_working_directory}'+'\\diary.txt'
diary_existence = os.path.isfile(path)
if diary_existence == False:
    diary = open("diary.txt", "x")
    diary.close()

with open(path, 'r') as file:                           #file = open("diary.txt", "r")
    print(f'Earlier entries:\n\n{file.read()}')         #a = file.read()
                                                        #print(f"Earlier entries:\n\n{a}")
new_entry = input('Please, type new diary entry:')      #file.close()

with open(path, 'a') as file:
    file.write(new_entry +'\n\n')
    print(f'\nNew diary entry:<{new_entry}>')
    print('\nDiary saved')