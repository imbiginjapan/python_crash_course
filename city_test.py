import unittest
from city_functions import format_location

class CityTestCase(unittest.TestCase):

	def test_city_country(self):
		formatted_loc = format_location('santiago','chile')
		self.assertEqual(formatted_loc,"Santiago, Chile")

	def test_city_country_population(self):
		formatted_loc = format_location('santiago','chile','600,000')
		self.assertEqual(formatted_loc,"Santiago, Chile Population 600,000")

unittest.main()
