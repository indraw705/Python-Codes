def DataManupulate(element):
	filterArr = list(filter(lambda no: no % 2 == 0 ,element))
	print(filterArr)
	squareNums = list(map(lambda no:(no**2),filterArr))
	print(squareNums)
	result = reduce(lambda no1, no2 : (no1+no2),squareNums)
	print(result)




elements = []
elementCount = int(input("Number of Elments : \n"))
print('Eneter Elements list : \n')
for i in range(elementCount):
	elements.append(int(input()))
print(elements)







# elements = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
DataManupulate(elements)