import unittest
from Testirovanie_chapter11 import Employee


class TestEmployee(unittest.TestCase):
    """Тест для класса Employee"""

    def setUp(self):
        """Создание опроса и набора ответов для всех тестовых методов"""
        self.annual_income = Employee("Volodia", "Rahmanov", 5000)
        self.annual_income.give_raise()
        self.annual_income.save_income()

    def test_give_default_raise(self):
        """Тест на ежегодное повышение в размере 5000"""
        pass

    def test_give_custom_raise(self):
        """Тест на индивидуалное повышение"""
        pass
