from itertools import permutations
def printpermutation(str1):
	permList = permutations(str1)
	for perm in list(permList):
		print (''.join(perm)) 
		

str1 = input("Enter any string \n")
printpermutation(str1)