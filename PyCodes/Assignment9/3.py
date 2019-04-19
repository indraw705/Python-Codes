def copyFile(file1, file2):
    fptr1 = open(file1, 'r+')
    content = fptr1.read()
    fptr2 = open(file2, 'w+')
    fptr2.write(content)
    fptr2.close()
    fptr1.close()


if __name__ == "__main__":
    copyFile("file1.txt", "file2.txt")
