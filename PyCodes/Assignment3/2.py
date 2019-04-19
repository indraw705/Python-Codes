

def PrintMaxNumber(elements):
	return max(elements)

elements = []
elementCount = int(input("Number of Elments : \n"))
print('Eneter Elements list : \n')
for i in range(elementCount):
	elements.append(int(input()))


print("Maximum number is  : {}".format(PrintMaxNumber(elements)))

