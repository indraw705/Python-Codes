# def decoratorFunc(originalFunc):
# 	def wrapperFunc(*args, **kwargs):
# 		print("I'm in Wrapper Func , executed before {} ".format(originalFunc.__name__))
# 		return originalFunc(*args, **kwargs)
# 	return wrapperFunc


class decoratorClass():
	"""docstring for decoratorClass"""
	def __init__(self, originalFunc):
		self.originalFunc = originalFunc
		
	def __call__(self, *args, **kwargs):
		print("I'm class decorator executed before the function {}".format(self.originalFunc.__name__))
		return self.originalFunc(*args, **kwargs)


@decoratorClass
def display():
	print("I'm display function")

@decoratorClass
def display_info(name, age):
	print("This method ran with 2 args {} and {}".format(name, age))

display_info("indrajit",56)
print("+++++++++++++++++++\n\n")
display() 