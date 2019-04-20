from sys import *
import os
import subprocess


def moveFilesWithExt(targetLoc, destLoc, exts):
    flag = os.path.isabs(targetLoc)
    if flag == True:
        targetLoc = os.path.abspath(targetLoc)
    t_exists = (os.path.isdir(targetLoc))
    flag = os.path.isabs(destLoc)
    if flag == True:
        destLoc = os.path.abspath(destLoc)
    d_exists = (os.path.isdir(destLoc))
    if not d_exists:
        subprocess.call(["mkdir", destLoc])

    if t_exists:
        for folderName, subFolders, files in os.walk(targetLoc):
            print("currentFolder is " + folderName)
            for file in files:
                if file.lower().endswith(exts):
                    print(file)
                    subprocess.call(["cp", os.path.abspath(folderName) + "/" + file, os.path.abspath(destLoc) + "/"])


def main():
    if (len(argv) != 4):
        print("Error : invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("this Application is designed for copying the file ")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage :copy the file")
        exit()

    try:
        moveFilesWithExt(argv[1], argv[2], argv[3])
    except ValueError:
        print("invalid Data type of input")
    except Exception as e:
        print("Error : Invalid input", e)


if __name__ == "__main__":
    main()
