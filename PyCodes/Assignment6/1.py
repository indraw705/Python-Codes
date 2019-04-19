class Demo:
	value = 1
	def __init__(self, no1, no2):
		self.no1 = no1
		self.no2 = no2

	def fun(self):
		print("no1 is {} and no2 is {}".format(self.no1, self.no2))


	def gun(self):
		print("no1 is {} and no2 is {}".format(self.no1, self.no2))


Obj1 = Demo(int(input("enter 2 numbers")),int(input()))
Obj2 = Demo(int(input("enter 2 numbers")),int(input()))


Obj1.fun()
Obj2.fun()
Obj1.gun()
Obj2.gun()