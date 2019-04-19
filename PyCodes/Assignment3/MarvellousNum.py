def CheckPrime(num):
	if num > 1:
		for i in range(2,num):	
			if (num % i)==0:
				return False
				break
		else:
			return True
	else:
		return False
print(CheckPrime(45))