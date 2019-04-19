

def returnFreqOfNum(elements,no):
	'''This will return freq of number from provided list'''
	count = 0
	for i in range(len(elements)):
		if elements[i] == no:
			count+=1
	return count


elements = []
elementCount = int(input("Number of Elments : \n"))
print('Eneter Elements list : \n')
for i in range(elementCount):
	elements.append(int(input()))

print("Accurence is  : {}".format(returnFreqOfNum(elements,int(input("enter number for check freq : \n ")))))
