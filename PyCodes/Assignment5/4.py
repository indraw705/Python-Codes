
def removeCharAtPosition(str,pos):
	listedStr = list(str)
	listedStr.pop(pos-1)
	finalStr=""
	for i in listedStr:
		finalStr+=i
	return (finalStr)
# str1 = "ABCDEFGHI"
# pos = 2
str1 = input("Enter String \n")
pos  = int(input('Position value \n'))
print(removeCharAtPosition(str1,pos))