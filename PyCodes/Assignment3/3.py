

def PrintMinNumber(elements):
	return min(elements)

elements = []
elementCount = int(input("Number of Elments : \n"))
print('Eneter Elements list : \n')
for i in range(elementCount):
	elements.append(int(input()))


print("Minimum number is  : {}".format(PrintMinNumber(elements)))

