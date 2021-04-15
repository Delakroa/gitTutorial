# from Testirovanie_chapter11 import get_formatted_name
#
# print("Введите 'q' для выхода в любое время. ")
# while True:
#     first = input("Пожалуйста введите ваше имя: ")
#     if first == "q":
#         break
#     last = input("Введите пожалуйста вашу фамилию: ")
#     print("")
#     if last == "q":
#         break
#     formatted_name = get_formatted_name(first, last)
#     print("\tАккуратно отформатированное имя: " + formatted_name + '.' + "\n")

# ----------------------------------------------------------------------------------------------------------------

import unittest
from Testirovanie_chapter11 import get_formatted_name


class NamesTestCase(unittest.TestCase):  # 1
    """Тесты для 'Testirovanie_chapter11.py'."""

    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formatted_name = get_formatted_name('janis', 'joplin')  # 2
        self.assertEqual(formatted_name, 'Janis Joplin')  # 3


if __name__ == '__main__':
    unittest.main()
