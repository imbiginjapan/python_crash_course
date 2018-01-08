import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	
	def test_first_last(self):
		formatted_name = get_formatted_name('joe','smith')
		self.assertEqual(formatted_name,"Joe Smith")
		
	def test_first_last_middle(self):
		formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name,"Wolfgang Amadeus Mozart")
	

unittest.main()
