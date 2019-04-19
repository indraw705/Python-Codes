def CalculateAvg(str):
	listArr = list(str)
	value = 0
	for i in listArr:
		value+=ord(i)
	return (value/len(listArr))


str1 = "ABCDE"
# pos = 2
# str1 = input("Enter String \n")
print("Avrage of ASCII value is " + str(CalculateAvg(str1)))