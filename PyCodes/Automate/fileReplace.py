

# f = open("indra.txt", "r+")
# lines = f.readlines()
# last_line = str(lines[-1])
# f.write(last_line.replace('}','\b\bindra'))
# print(last_line)

f = open("indra.txt", "r+")
lines = f.readlines()
str1=""
for line in lines:
	str1+=str(line)
f.close()
f = open("indra.txt", 'w')
f.write(str1[:-1])
f.write("<>insert code here that you want <> }")
f.close()