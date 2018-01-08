import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	
	def test_give_default_raise(self):
		employee = Employee("John","Smith",50000.00) 
		salary = employee.salary
		employee.give_raise()
		self.assertEqual(employee.salary, salary + 5000.00)
	
	def test_give_custom_raise(self):
		employee = Employee("John","Smith",50000.00) 
		salary = employee.salary
		custom = 2500.00
		employee.give_raise(custom)
		self.assertEqual(employee.salary, salary + custom)
	
		
unittest.main()
		
