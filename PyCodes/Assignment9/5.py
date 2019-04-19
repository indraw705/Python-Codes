
def searchWord(filename, text):
    fp = open(filename, 'r+')
    content = fp.read()
    counts = dict()
    words = content.split()
    for word in words:
        if word in counts:
            counts[word] += 1

        else:
            counts[word] = 1

    return counts[text]


try:
    print("freq of word is : {}".format(searchWord("file1.txt", "program")))
except KeyError as k:
    print("word not found")
