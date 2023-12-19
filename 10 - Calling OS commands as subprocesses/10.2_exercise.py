#2) Write a program that lists the contents of a given directory just like "ls -l" would 
#   but filter out all lines containing the string 'banana'. Implement the filtering on Python side.
import random
import argparse
import os

def create_files():
# create a group of files with random names:
    file_names = ["banana.txt", "test.txt", "document.txt", "test_doc.txt", "example.txt", "banana_log.txt", "banana_doc.txt"]
    files_list = []
    
    for num in range(random.randint(10,20)):
        files_list.append(str(num + 1) + "_" + random.choice(file_names))

    # convert a file_names list to string:
    parameters = " "
    parameters = parameters.join(files_list)

    pipe_handle1 = os.popen(f"touch {parameters}; ls -l")
    print(f"Output of 'touch {parameters}; ls -l' command:")
    for line in pipe_handle1:
        line = line.replace("\n", "")
        print(line)
    return parameters

def create_parser():
    parser = argparse.ArgumentParser(description='Lists the contents of a given directory')
    # positional command line argument
    parser.add_argument('path', type=str, help='Define absolute (full) path to the directory')
    return parser

def sort_list(arg):
    pipe_handle2 = os.popen(f"ls -l {arg}")
    print(f"\nOutput of 'ls -l {arg}' command:")
    for line in pipe_handle2:
        if "banana" in line:
            line = line.replace("\n", "")
            print(line)
        else:
            continue
    print("End of the script.")

def remove_files(parameters):
    # remove the files:
    os.system(f"rm {parameters}")

if __name__ == '__main__':
    parameters = create_files()
    parser = create_parser()
    args = parser.parse_args()
    arg = args.path
    sort_list(arg)
    remove_files(parameters)