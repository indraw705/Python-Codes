import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
	def log_func(*args):
		logging.info('Running "{}" with Arguments {}'.format(func.__name__, args))
		print(func(*args))
	return log_func



def add(a, b):
	return a+b


def sub(a, b):
	return a-b


add_logger = logger(add)
sub_logger = logger(sub)



add_logger(1,3)
add_logger(10,35)


sub_logger(100,35)
sub_logger(20,15)