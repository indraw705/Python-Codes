class Arithmetic:


	def __init__(self, val1=0, val2=0):
		self.val1 = val1
		self.val2 = val2
		

	def Accept(self):
		self.val1 , self.val2 = int(input("Enter 2 values ")),int(input("\n"))
	def Addition(self):
		return (self.val1 + self.val2)
	def Subtraction(self):
		return (self.val1 - self.val2)
	def Multiplication(self):
		return (self.val1 * self.val2)
	def Division(self):
		return (self.val1 / self.val2)
		

obj1 = Arithmetic()

obj1.Accept()
print(obj1.Addition())
print(obj1.Subtraction())
print(obj1.Multiplication())
print(obj1.Division())