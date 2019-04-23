'''1.Design automation script which accept directory name and display checksum of all files.
Usage : DirectoryChecksum.py “Demo”
Demo is name of directory.
'''



from sys import *
import os
import hashlib


def file_as_bytes(file):
    with file:
        return file.read()


def allFileCheckSum(path):
    flag = os.path.isabs(path)
    if flag == True:
        path = os.path.abspath(path)
    exists = (os.path.isdir(path))
    if exists:
        for folderName, subfolder, files in os.walk(path):
            for file in files:
                print("Checksum of File {} is {} \n".format(file, hashlib.md5(file_as_bytes(open(os.path.abspath(folderName) + "/" + file, 'rb'))).hexdigest()))
    else:
        print("invalid path")


def main():

    if (len(argv) != 2):
        print("Error : invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("this Application is designed for Generating md5 Checksum")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage :Checksum the file")
        exit()

    try:
        allFileCheckSum(argv[1])
    except ValueError:
        print("invalid Data type of input")
    except Exception as e:
        print("Error : Invalid input", e)


if __name__ == "__main__":
    main()
