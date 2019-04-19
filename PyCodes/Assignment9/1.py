from os import path


def checkFilePresentOrNot(filename):
    print("file is present") if path.exists(filename) else print("file not found")


filename = "indra.txt"
checkFilePresentOrNot(filename)
