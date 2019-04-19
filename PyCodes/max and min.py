a = [91,521,11112,7,10,4411,32111,844,25,3,125]

max = 0
min = a[0]
for i in range(0,len(a)):
    if max < a[i]:
        max = a[i]
    if min > a[i]:
        min = a[i]


print('min value is :'+ str(min))
print('max value is :'+ str(max))