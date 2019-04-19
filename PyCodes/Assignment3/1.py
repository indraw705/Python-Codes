
# def add(*args):
# 	return sum(args)

# print(add(1,2,3,4))
# print(add(12,3,1,2,31,23,1,2,1,1,3,4,3,13))
# print(add(11,22,33,44))
# print(add(10,20,30,40))




elements = []
elementCount = int(input("Number of Elments : \n"))
print('Eneter Elements list : \n')
for i in range(elementCount):
	elements.append(int(input()))
	print(elements)
print("Sum of elements are : {}".format(sum(elements)))

