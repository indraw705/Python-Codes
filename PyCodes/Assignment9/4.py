'''
4.Write a program which accept two file names from user and compare contents of both the
files. If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
Input : Demo.txt Hello.txt
Compare contents of Demo.txt and Hello.txt
'''


def compareFile(file1, file2):
    fptr1 = open(file1, 'r+')
    content1 = fptr1.read()
    fptr2 = open(file2, 'r+')
    content2 = fptr2.read()
    fptr2.close()
    fptr1.close()

    return content1 == content2


if __name__ == "__main__":
    status = compareFile("file1.txt", "indra.txt")
    print("yes those files are same") if status == True else print("files are different")
