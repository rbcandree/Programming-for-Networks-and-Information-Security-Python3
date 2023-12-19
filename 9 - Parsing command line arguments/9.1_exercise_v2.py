# Implement a program that takes a filename as a positional command line argument 
# and appends the string given by optional command line argument --input to the end of that file.
# If the --input argument is not given, overwrite the given file's content 
# with the string: "Beginning of input stash:\n"

import argparse

def create_parser():
    parser = argparse.ArgumentParser(description='Adds new lines into a text file')
    
    #1st positional command line argument
    parser.add_argument('filename', type=argparse.FileType('r'), help='Input text file')
    
    #2nd optional command line argument
    parser.add_argument('--input', type=str, help='Input text file')
    
    return parser           

def edit_file(arg1, arg2):
    if args.input is None:
        with open(arg1.name, 'w') as f:
            f.write("Beginning of input stash:\n")
    else:
        with open(arg1.name, 'a') as f:
            f.write(f"{arg2}\n")

def read_file(arg1):
    with open(arg1.name, 'r') as f:
        print(f.read())

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    arg1 = args.filename
    arg2 = args.input
    edit_file(arg1, arg2)
    read_file(arg1)