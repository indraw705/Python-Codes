from MarvellousNum import CheckPrime


def additionOfPrimeNums(elements):
	total = 0
	for i in range(len(elements)):
		if CheckPrime(elements[i])==True:
			print(elements[i])
			total = total + elements[i]
	return total

elements = []
elementCount = int(input("Number of Elments : \n"))
print('Eneter Elements list : \n')
for i in range(elementCount):
	elements.append(int(input()))
print(elements)

print('sum of elements are {} '.format(additionOfPrimeNums(elements)))
4

