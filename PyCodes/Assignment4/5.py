from MarvellousNum import CheckPrime

def DataManupulate(element):
	filterArr = list(filter(lambda no:CheckPrime(no),element))
	print(filterArr)
	add10arr = list(map(lambda no:(no*2),filterArr))
	print(add10arr)
	result = reduce(lambda no1,no2 : max(no1,no2),add10arr)
	print(result)

list1 = [2, 70 , 11, 10, 17, 23, 31, 77]
DataManupulate(list1)