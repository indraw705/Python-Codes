class Employee():
	raise_amount = 1.20
	def __init__(self, first , last , pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullName(self):
		return '{} {}'.format(self.first, self.last)

	def applyRaise(self):
		self.pay = int(self.pay * self.raise_amount) 

	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first , last, pay = emp_str.split('_')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return 'No'
		return 'Yes'


class Developer(Employee):
	raise_amount = 1.40

	def __init__(self, first , last , pay, prog_lang):
		super().__init__(first , last, pay)
		self.prog_lang = prog_lang
		

class Manager(Employee):
	def __init__(self, first , last , pay, employees=None):
		super().__init__(first , last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
		
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
	
	def print_emps(self):
		for emp in self.employees:
			print('>--->'+ emp.fullName())

dev1 = Developer('Indrajit', 'Narvekar', 7000, 'python')
dev2 = Developer('Mayur', 'Jadhav', 8000, 'JAVA')

print(dev2.email)
print(dev2.prog_lang)

mgr1 = Manager('bharat', 'C', 5600, [dev1])

mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)
print(mgr1.email)
print(mgr1.print_emps())

# emp1 = Employee('Indrajit', 'Narvekar', 7000)
# emp2 = Employee('Mayur', 'Jadhav', 8000)

# emp_str_1 = 'Mayur_Singh_7000'
# emp_str_2 = 'Indrajit_Narveker_5000'
# emp_str_3 = 'Bharat_Jadhav_7200'

# new_employee1 = Employee.from_string(emp_str_1)
# new_employee2 = Employee.from_string(emp_str_2)
# new_employee3 = Employee.from_string(emp_str_3)

# print(new_employee2.email)

# import datetime

# my_date = datetime.date(2019, 3, 10)
# print(Employee.is_workday(my_date))

# Employee.set_raise_amount(1.15)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)