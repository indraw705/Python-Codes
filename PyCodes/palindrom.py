def isPalindrom(str):
    return str[::-1] == str


a = "madam"
status = isPalindrom(a)
print("yes") if status == True else print("No")
