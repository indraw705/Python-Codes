def DataManupulate(element):
	filterArr = list(filter(lambda no: (90>no>70 ),element))
	print(filterArr)
	add10arr = list(map(lambda no:(no+10),filterArr))
	print(add10arr)
	result = reduce(lambda no1, no2 : (no1*no2),add10arr)
	print(result)


list1 = [100,71,91,8,4,76,35,78,51,88,75,68,48,89,49,68,65]
DataManupulate(list1)