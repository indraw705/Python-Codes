marksheet = {}
for _ in range(0,int(input())):
	marksheet.update({input() : [float(input()),float(input()),float(input())]})


print(marksheet)
student = input()

avarage = (marksheet[student][0]+marksheet[student][1]+marksheet[student][2])/3
print(('{0:.2f}'.format(float(avarage))))