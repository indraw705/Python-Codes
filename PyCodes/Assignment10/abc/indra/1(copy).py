from sys import *
import os


def DirectroryWatcher(path, exts):
    flag = os.path.isabs(path)
    if flag == True:
        path = os.path.abspath(path)
    exists = (os.path.isdir(path))
    if exists:
        for foldername, subfolder, files in os.walk(path):
            for file in files:
                if file.lower().endswith(exts):
                    print("files present for" + exts + " in \n" + foldername + " are : \n" + file)
                    
        # if flag == False:
        #     print("files with " + exts + " extenssion not in this dir")

    else:
        print("invalid path")


def main():

    if (len(argv) != 3):
        print("Error : invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("this Application is designed for finding the file with extenssion")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage :search the file")
        exit()

    try:
        DirectroryWatcher(argv[1], argv[2])
    except ValueError:
        print("invalid Data type of input")
    except Exception as e:
        print("Error : Invalid input", e)


if __name__ == "__main__":
    main()
