from sys import *
import os


def DirectroryWatcher(path):
    print(path)
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = (os.path.isdir(path))
    print(path)
    if exists:
        for foldername, subfolder, files in os.walk(path):
            print("currentFolder is " + foldername)
            for subf in subfolder:
                print("subfolder of " + foldername + " is " + subf)
            for file in files:
                print("files present in " + foldername + " are" + file)
            print("\n\n\n\n")

        print(' ')
    else:
        print("invalid path")


def main():
    print("Application name " + argv[0])

    if (len(argv) != 2):
        print("Error : invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("this Application is designed for Traversing the path")
        exit()
    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage :Application name absolute path")
        exit()

    try:
        DirectroryWatcher(argv[1])
    except ValueError:
        print("invalid Data type of input")
    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
