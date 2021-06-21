import unittest
from Testirovanie_chapter11 import description_cities


class CityCountryTestCase(unittest.TestCase):
    """Тест задания """

    def test_city_country(self):
        """Тестирование значения"""
        full_description = description_cities('santiago', 'chile')
        self.assertEqual(full_description, 'Santiago Chile')

    def test_city_country_population(self):
        """Проверка третьего аргумента 'населения'"""
        full_description = description_cities('santiago', 'chili', '5000000')
        self.assertEqual(full_description, 'Santiago Chili 5000000')


if __name__ == '__main__':
    unittest.main()
