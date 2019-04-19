import multiprocessing
import os

def fun(num):
	print("parent process of fun {}".format(os.getppid()))
	print("process id of fun {}".format(os.getpid()))
	for i in range(num):
		print(i)

def gun(num):
	print("parent process of gun {}".format(os.getppid()))
	print("process id of gun {}".format(os.getpid()))
	for i in range(num):
		print(i)

if __name__=="__main__":
	print("total cores available : {}".format(os.cpu_count()))
	print("parent process of main {}".format(os.getppid()))
	print("process id of main {}".format(os.getpid()))
	num = 4
	result = None

	p1 = multiprocessing.Process(target=fun,args=(num,))
	p2 = multiprocessing.Process(target=gun,args=(num,))


	p1.start()
	p2.start()

	p1.join()
	p2.join()