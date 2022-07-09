import unittest
from city_functions import city_country

class CountryTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_country = city_country('chile', 'santiago')
        self.assertEqual(formatted_city_country, 'Chile, Santiago')

if __name__ == '__main__':
    unittest.main()
