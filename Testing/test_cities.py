import unittest
from city_functions import city_country


class CountryTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_country = city_country('chile', 'santiago')
        self.assertEqual(formatted_city_country, 'Chile, Santiago')

    def test_city_country_population(self):
        formatted_city_country = city_country('chile', 'santiago', '30000')
        self.assertEqual(formatted_city_country, 'Chile, Santiago Population - 30000')

if __name__ == '__main__':
    unittest.main()
