"""
Write a program that expects any number of filenames as arguments, and indicates the mean 
number of bytes per character in the content of each file, utilizing the command line as
follows:

$ python3 encode.py <filename>...

"""

import sys

def read_file(file):
    """Opens the file designated by user and reads it."""

    # Checks whether file exists. If not, porgram is aborted.
    try:
        with open(file, 'rb') as f:
            data = f.read()
            return data
    except FileNotFoundError:
        raise(SystemExit)(f"The {file} file does not exist. Please try another file.")


def count_char(data):
    """Calculates character count for file by converting the bytes to characters."""

    try:
        return len(data.decode())
    except:
        return len(data)


if __name__ == '__main__':

    """Checks whether file name was provided. If not, SystemExit rather than
    IndexError is used to abort the program"""
    try:
        filename = sys.argv[1]
    except IndexError:
        raise(SystemExit)("Filename must be provided on the command line.")

    total_bytes = total_char = num_files = 0
    
    for i in sys.argv[1:]:
        data = read_file(i)
        total_bytes += len(data)
        total_char += count_char(data)
        num_files += 1

    print("The mean is {} bytes/characters per file.".format(total_bytes/total_char/num_files))