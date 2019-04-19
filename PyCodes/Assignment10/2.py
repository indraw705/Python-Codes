from sys import *
import os


def DirectroryWatcher(path, exts, replaceexts):
    '''Replace the existing extenssion to new one provided by user'''
    flag = os.path.isabs(path)
    if flag == True:
        path = os.path.abspath(path)
    exists = (os.path.isdir(path))
    if exists:
        for foldername, subfolder, files in os.walk(path):
            print("currentFolder is " + foldername)
            for file in files:
                if file.lower().endswith(exts):
                    base = os.path.splitext(file)[0]
                    os.rename(os.path.abspath(foldername) + "//" + file, os.path.abspath(foldername) + "//" + base + replaceexts)
    else:
        print("invalid path")


def main():
    '''The main  entry point'''

    if (len(argv) != 4):
        print("Error : invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("this Application is designed for finding the file with extenssion")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage :search the file")
        exit()

    try:
        DirectroryWatcher(argv[1], argv[2], argv[3])
    except ValueError:
        print("invalid Data type of input")
    except Exception as e:
        print("Error : Invalid input", e)


if __name__ == "__main__":
    main()
