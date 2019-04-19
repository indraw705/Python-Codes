import threading


def even(num):
	for i in range(0,num):
		if  i%2 == 0:
			print(i)

def odd(num):
	for i in range(0,num):
		if  i%2 != 0:
			print(i)


if __name__ == "__main__":
	num = 20
	thread1 = threading.Thread(target=even, args=(num,))
	thread2 = threading.Thread(target=odd, args=(num,))
	
	
	thread1.start()
	thread2.start()
	
	thread1.join()
	thread2.join()