import unittest
from Testirovanie_chapter11 import Employee


class TestEmployee(unittest.TestCase):
    """Тест для класса Employee"""

    def setUp(self):
        """Создание опроса и набора ответов для всех тестовых методов"""
        self.volodia = Employee("Volodia", "Rahmanov", 65000)

    def test_give_default_raise(self):
        """Проверить правильность работы повышения"""
        self.volodia.give_raise()
        self.assertEqual(self.volodia.annual_salary, 70000)

    def test_give_custom_raise(self):
        """Проверить правильность работы индивидуального повышения"""
        self.volodia.give_raise(10000)
        self.assertEqual(self.volodia.annual_salary, 75000)


if __name__ == '__main__':
    unittest.main()
