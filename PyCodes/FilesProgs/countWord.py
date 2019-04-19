str1 = 'guruprasad chandrashekar patil'
str1 = str1.replace(' ','')
dict1 = dict()
for i in range(0,len(str1)):
	count = 0
	for j in range(0,len(str1)):
		if str1[i] == str1[j]:
			count = count + 1
		
	dict1[str1[i]]=count
print(dict1)

