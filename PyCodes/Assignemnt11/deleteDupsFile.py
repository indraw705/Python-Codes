'''3. Design automation script which accept directory name and delete all duplicate files from that
directory. Write names of duplicate files from that directory into log file named as Log.txt.
Log.txt file should be created into current directory.
Usage : DirectoryDusplicateRemoval.py “Demo”
'''


from sys import *
import os
import hashlib
import subprocess


def file_as_bytes(file):
    with file:
        return file.read()


def findDupsFiles(path):
    print(path)
    checksums = dict()
    duplicateFiles = list()
    flag = os.path.isabs(path)
    if flag == True:
        path = os.path.abspath(path)
    exists = (os.path.isdir(path))
    if exists:
        for folderName, subfolder, files in os.walk(path):
            for file in files:
                checkSumofFile = hashlib.md5(file_as_bytes(open(os.path.abspath(folderName) + "/" + file, 'rb'))).hexdigest()
                if checkSumofFile in checksums.values():
                    print("{} is duplicate having checksum = {} ".format(file, checkSumofFile))
                    duplicateFiles.append(file)
                    with open("op.txt", "w") as fp:
                        fp.write("duplicate files is as follow \n")
                        fp.write(str(duplicateFiles))

                else:
                    checksums[os.path.abspath(folderName) + "/" + file] = checkSumofFile
            for file in duplicateFiles:
                subprocess.call(["rm", os.path.abspath(folderName) + "/" + file])
                # print("Checksum of File {} is {} \n".format(file, hashlib.md5(file_as_bytes(open(os.path.abspath(folderName) + "/" + file, 'rb'))).hexdigest()))
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
        findDupsFiles(argv[1])

    except ValueError:
        print("invalid Data type of input")
    except Exception as e:
        print("Error : Invalid input", e)


if __name__ == "__main__":
    main()
