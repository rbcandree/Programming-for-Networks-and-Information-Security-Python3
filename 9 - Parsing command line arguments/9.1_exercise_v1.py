# Implement a program that takes a filename as a positional command line argument 
# and appends the string given by optional command line argument --input to the end of that file.
# If the --input argument is not given, overwrite the given file's content 
# with the string: "Beginning of input stash:\n"

import argparse
import sys

try:
    parser = argparse.ArgumentParser(description='Adds new lines into a text file')
    
    #1st positional command line argument
    parser.add_argument('filename', type=argparse.FileType('r'), help='Input text file')
    
    #2nd optional command line argument
    parser.add_argument('--input', type=str, help='Input text file')

    args = parser.parse_args()
    arg1 = args.filename
    arg2 = args.input

except Exception:
    print(parser.print_usage())
    sys.exit(1)

if args.input is None:
    with open(arg1.name, 'w') as f:
        f.write("Beginning of input stash:\n")
else:
    with open(arg1.name, 'a') as f:
        f.write(f"{arg2}\n")

#Display a text file
with open(arg1.name, 'r') as f:
    print(f.read())