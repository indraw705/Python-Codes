import re


def passwordStrngth(str):
	# if checkCount(re.compile(r'[a-z]')) == True:
	# 	pass
	# else:
	# 	print("Password should contain 1 small characher")
	# if checkCount(re.compile(r'[A-Z]')) == True:
	# 	pass
	# else:
	# 	print("Password should contain 1 Capital characher")
	# if checkCount(re.compile(r'[\d]')) == True:
	# 	pass
	# else:
	# 	print("Password should contain 1 number characher")
	# if checkCount(re.compile(r'[!@$%&*]')) == True:
	# 	pass
	# else:
	# 	print("Password should contain 1 speacial characher")
	if checkCount(re.compile(r'([a-z])([A-Z])([!@$%&])([\d])')) == True:
		pass
	else:
		print("Password should contain 1 indra")

def checkCount(pattern):
	matches = pattern.finditer(words)
	for match in matches:
		print(match.group(1))

	# if (len(list(matches))) > 0:
	# 	return True
	# else:	
	# 	return False



words = '''
asdasd'''

passwordStrngth(words)
