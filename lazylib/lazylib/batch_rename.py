import argparse
import os
from termcolor import colored, cprint

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-i", "--input", help="input_path")
parser.add_argument("-p", "--pattern", help="basename_for_renaming")
parser.add_argument("-n", "--number", default=0, type=int, help="starting_index_number")

# Read arguments from command line
args = parser.parse_args()

path = args.input
pattern = args.pattern
number = args.number
if os.path.exists(path):
    files = os.listdir(path)

    for index, file in enumerate(files):
        basename, file_ext = os.path.splitext(file)
        file_name = pattern + "_" + str(number + index) + file_ext
        print(file_name)
        os.rename(os.path.join(path, file), os.path.join(path, file_name))
else:
    cprint("The Given Path Doesn't Exists", 'white', 'on_red')
