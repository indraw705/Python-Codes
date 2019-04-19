import time

ef_cache = {}

def expensive_func(num):
	if num in ef_cache:
		return ef_cache[num]
	print("Computing results for {}".format(num))
	time.sleep(2)
	result = num*num
	ef_cache[num] = result
	return result



result = expensive_func(10)
print(result)
result = expensive_func(15)
print(result)
result = expensive_func(10)
print(result)
result = expensive_func(13)
print(result)
result = expensive_func(14)
print(result)
result = expensive_func(12)
print(result)
result = expensive_func(13)
print(result)
result = expensive_func(10)
print(result)
result = expensive_func(15)
print(result)