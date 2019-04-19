def printFileContents(fName):
    fd = open(fName, 'r+')
    content = fd.read()
    print(content)


fName = "indra.txt"
printFileContents(fName)
