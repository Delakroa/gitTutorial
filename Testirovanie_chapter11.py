# 11 Тестирование

# Вместе с функциями и классами вы также можете написать тесты для своего кода.
# Тестирование доказывает, что код работает так, как положено, для любых разно-
# видностей входных данных, которые он может получать. Тесты позволят вам быть
# уверенным в том, что код будет работать правильно и тогда, когда вашими про-
# граммами станут пользоваться другие люди. Тестирование при добавлении нового
# кода гарантирует, что внесенные изменения не повлияют на текущее поведение
# программы. Все программисты допускают ошибки, поэтому каждый программист
# должен часто тестировать свой код и выявлять ошибки до того, как с ними столкнутся
# другие пользователи.
# В этой главе вы научитесь тестировать код средствами модуля Python unittest.
# Вы узнаете, как построить тестовые сценарии, как проверить, выдает ли программа
# для конкретных входных данных ожидаемый результат и как тестировать функ-
# ции и классы. Также вы научитесь оценивать, сколько тестов нужно написать для
# проекта.

# ---------------------------------------------------------------------------------------------------------------------

# Тестирование функции

# Чтобы потренироваться в тестировании, нам понадобится код. Ниже приведена
# простая функция, которая получает имя и фамилию и возвращает отформатиро-
# ванное полное имя:

# def get_formatted_name(first, last):
#     """Строит отформатированное полное имя"""
#     full_name = first + ' ' + last
#     return full_name.title()


# Функция get_formatted_name() строит полное имя из имени и фамилии, разде-
# лив их пробелом, преобразует первый символ каждого слова к верхнему регистру
# и возвращает полученный результат. Чтобы убедиться в том, что функция get_
# formatted_name() работает правильно, мы напишем программу, использующую
# эту функцию. Программа names.py запрашивает у пользователя имя и фамилию
# и выдает отформатированное полное имя:

# from name_function import get_formatted_name


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
#     print("\tАккуратно отформатированное имя: " + formatted_name + '.')

# Программа импортирует функцию g e t _ f o r m a t t e d _ n a m e ( ) из модуля

# name_function.py. Пользователь вводит последовательность имен и фамилий
# и видит,
# что программа сгенерировала отформатированные полные имена:
#
#
# Enter 'q' at any time to quit.
# Please give me a first name: janis
# Please give me a last name: joplin
# Neatly formatted name: Janis Joplin.
# Please give me a first name: bob
# Please give me a last name: dylan
# Neatly formatted name: Bob Dylan.
# Please give me a first name: q

# Как видно из листинга, имена сгенерированы правильно. Но допустим, вы решили
# изменить функцию get_formatted_name(), чтобы она также работала со вторыми
# именами. При этом необходимо проследить за тем, чтобы функция не перестала
# правильно работать для имен, состоящих только из имени и фамилии. Чтобы про-
# тестировать код, можно запустить names.py и для проверки вводить имя из двух
# компонентов (скажем, Janis Joplin) при каждом изменении get_formatted_name(),
# но это довольно утомительно. К счастью, Python предоставляет эффективный
# механизм автоматизации тестирования вывода функций. При автоматизации те-
# стирования get_formatted_name() вы будете уверены в том, что функция успешно
# работает для всех видов имен, для которых написаны тесты.

# -------------------------------------------------------------------------------------------------------------------

# Прохождение теста

# Вы не сразу привыкнете к синтаксису создания тестовых сценариев, но после того,
# как тестовый сценарий будет создан, вы сможете легко добавить новые модульные
# тесты для своих функций. Чтобы написать тестовый сценарий для функции, импор-
# тируйте модуль unittest и функцию, которую необходимо протестировать. Затем
# создайте класс, наследующий от unittest.TestCase, и напишите серию методов для
# тестирования различных аспектов поведения своей функции.
# Ниже приведен тестовый сценарий с одним методом, который проверяет, что функ-
# ция get_formatted_name() правильно работает при передаче имени и фамилии:

# import unittest
# from Testirovanie_chapter11 import get_formatted_name
#
#
# class NamesTestCase(unittest.TestCase):   # 1
#     """Тесты дял 'Testirovanie_chapter11.py'."""
#
#     def test_first_last_name(self):
#         """Имена вида 'Janis Joplin' работают правильно?"""
#         formatted_name = get_formatted_name('janis', 'joplin')   # 2
#         self.assertEqual(formatted_name, 'Janis Joplin')    # 3
#
#
# unittest.main()

# Сначала мы импортируем unittest и тестируемую функцию get_formatted_name().
# В точке  создается класс NamesTestCase, который содержит серию модульных
# тестов для get_formatted_name(). Имя класса выбирается произвольно, но лучше
# выбрать имя, связанное с функцией, которую вы собираетесь тестировать, и вклю-
# чить в имя класса слово Test. Этот класс должен наследовать от класса unittest.
# TestCase, чтобы Python знал, как запустить написанные вами тесты.
# Класс NamesTestCase содержит один метод, который тестирует всего один аспект
# get_formatted_name() — правильность форматирования имен, состоящих только из
# имени и фамилии. Мы назвали этот метод test_first_last_name(). Любой метод,
# имя которого начинается с test_, будет выполняться автоматически при запуске
# test_name_function.py. В тестовом методе вызывается тестируемая функция и сохра-
# няется возвращаемое значение, которое необходимо проверить. В данном примере
# вызывается функция get_formatted_name() с аргументами 'janis' и 'joplin',
# а результат сохраняется в переменной formatted_name .
# В точке  используется одна из самых полезных особенностей unittest: метод
# assert. Методы assert проверяют, что полученный результат соответствует тому
# результату, который вы рассчитывали получить. В данном случае известно, что
# функция get_formatted_name() должна вернуть полное имя с пробелами и капита-
# лизацией слов, поэтому переменная formatted_name должна содержать текст «Janis
# Joplin». Чтобы убедиться в этом, мы используем метод assertEqual() из модуля
# unittest и передаем ему переменную formatted_name и строку 'Janis Joplin'.
# Вызов
# self.assertEqual(formatted_name, 'Janis Joplin')
# означает: «Сравни значение formatted_name со строкой 'Janis Joplin'. Если они
# равны, как и ожидалось, — хорошо. Но если они не равны, обязательно сообщи
# мне!»
# Строка unittest.main() приказывает Python выполнить тесты из этого файла.
# При запуске test_name_function.py будет получен следующий результат:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK
#
# Точка в первой строке вывода сообщает, что один тест прошел успешно. Следу-
# ющая строка говорит, что для выполнения одного теста Python потребовалось
# менее 0,001 секунды. Наконец, завершающее сообщение OK говорит о том, что все
# модульные тесты в тестовом сценарии прошли.
# Этот результат показывает, что функция get_formatted_name() успешно работает
# для полных имен, состоящих из имени и фамилии, если только функция не была
# изменена. В случае внесения изменений в get_formatted_name() тест можно запу-
# стить снова. И если тестовый сценарий снова пройдет, мы будем знать, что функция
# продолжает успешно работать с полными именами из двух компонентов.

# --------------------------------------------------------------------------------------------------------------------

# Сбой теста

# Как выглядит сбойный тест? Попробуем изменить функцию get_formatted_name(),
# чтобы она работала со вторыми именами, — но сделаем это так, чтобы она перестала
# работать с полными именами из двух компонентов.
# Новая версия get_formatted_name() с дополнительным аргументом второго имени
# выглядит так:



def get_formatted_name(first, middle, last):
    """Строит отформатированное полное имя."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
