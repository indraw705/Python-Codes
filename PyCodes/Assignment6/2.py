class Circle:

	PI = 3.1416

	def __init__(self, radius=0 , Area=0, Circumference=0):
		self.radius = radius
		self.Area = Area
		self.Circumference = Circumference

	def Accept(self):
		self.radius = float(input("Enter radius value \n"))
		# self.Radius = Radius

	def CalculateArea(self):
		self.Area = self.PI*self.radius**2


	def CalculateCircumference(self):
		self.circumference = 2*self.PI*self.radius


	def Display(self):
		print("Area of circl is {} and circumference is {} for radius is equal to {}".format(self.Area, self.circumference, self.radius))


obj1 = Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()