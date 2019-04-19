import threading

def fun(num):
	for i in range(num):
		print("fun - {}".format(i))

def gun(num):
	for i in range(num):
		print("gun - {}".format(i))
		

if __name__=="__main__":
	number = 10
	thread1 = threading.Thread(target=fun, args=(number,))
	thread2 = threading.Thread(target=gun, args=(number,))
	# Will execute both in parallel
	thread1.start()
	thread2.start()
	# Joins threads back to the parent process, which is this
	# program
	thread1.join()
	thread2.join()