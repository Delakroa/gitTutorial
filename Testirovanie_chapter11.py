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


# def get_formatted_name(first, middle, last):
#     """Строит отформатированное полное имя."""
#     full_name = first + ' ' + middle + ' ' + last
#     return full_name.title()


# Эта версия должна работать для полных имен из трех компонентов, но тестирова-
# ние показывает, что она перестала работать для полных имен из двух компонентов.
# На этот раз файл test_name_function.py выдает следующий результат:


#  E
# ======================================================================
#  ERROR: test_first_last_name (__main__.NamesTestCase)
# ----------------------------------------------------------------------
#  Traceback (most recent call last):
# File "test_name_function.py", line 8, in test_first_last_name
# formatted_name = get_formatted_name('janis', 'joplin')
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'
# ----------------------------------------------------------------------
#  Ran 1 test in 0.000s
#  FAILED (errors=1)


# На этот раз информации гораздо больше, потому что при сбое теста разработчик
# должен знать, почему это произошло. Вывод начинается с одной буквы E , которая
# сообщает, что один модульный тест в тестовом сценарии привел к ошибке. Затем мы
# видим, что ошибка произошла в тесте test_first_last_name() в NamesTestCase .
# Конкретная информация о сбойном тесте особенно важна в том случае, если тестовый
# сценарий состоит из нескольких модульных тестов. В точке  мы видим стандартную
# трассировку, из которой понятно, что вызов функции get_formatted_name('janis',
# 'joplin') перестал работать из-за необходимого позиционного аргумента.
# Также из вывода следует, что был выполнен один модульный тест . Наконец, до-
# полнительное сообщение информирует, что тестовый сценарий в целом не прошел
# и произошла одна ошибка при выполнении тестового сценария . Эта информация
# размещается в конце вывода, чтобы она была видна сразу; разработчику не придется
# прокручивать длинный протокол, чтобы узнать количество сбойных тестов.

# ---------------------------------------------------------------------------------------------------------------------

# Реакция на сбойный тест

# Что делать, если тест не проходит? Если предположить, что проверяются правильные
# условия, прохождение теста означает, что функция работает правильно, а сбой — что
# в новом коде добавилась ошибка. Итак, если тест не прошел, изменять нужно не тест,
# а код, который привел к сбою теста. Проанализируйте изменения, внесенные в функ-
# цию, и разберитесь, как они привели к нарушению ожидаемого поведения.
# В данном случае у функции get_formatted_name() было всего два обязательных
# параметра: имя и фамилия. Теперь она требует три обязательных параметра: имя,
# второе имя и фамилию. Добавление обязательного параметра для второго имени
# нарушило ожидаемое поведение get_formatted_name(). В таком случае лучше все-
# го сделать параметр второго имени необязательным. После этого тесты для имен
# с двумя компонентами снова будут проходить, и программа сможет получать также
# вторые имена. Изменим функцию get_formatted_name(), чтобы параметр второго
# имени перестал быть обязательным, и снова выполним тестовый сценарий. Если
# он пройдет, можно переходить к проверке правильности обработки вторых имен.
# Чтобы сделать второе имя необязательным, нужно переместить параметр middle
# в конец списка параметров в определении функции и задать ему пустое значение
# по умолчанию. Также будет добавлена проверка if, которая правильно строит
# полное имя в зависимости от того, передается второе имя или нет:

# def get_formatted_name(first, last, middle=''):
#     """Строит отформатированное полное имя."""
#     if middle:
#         full_name = first + ' ' + middle + ' ' + last
#     else:
#         full_name = first + ' ' + last
#     return full_name.title()


# В новой версии get_formatted_name() параметр middle не обязателен. Если второе
# имя передается функции (if middle:), то полное имя будет содержать имя, второе
# имя и фамилию. В противном случае полное имя состоит только из имени и фа-
# милии. Теперь функция должна работать для обеих разновидностей имен. Чтобы
# узнать, работает ли функция для имен из двух компонентов, снова запустите
# test_name_function.py:

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK

# Теперь тестовый сценарий проходит. Такой исход идеален; он означает, что функ-
# ция снова работает для имен из двух компонентов и нам не пришлось тестировать
# функцию вручную. Исправить ошибку было несложно, потому что сбойный тест
# помог выявить новый код, нарушивший существующее поведение.

# ---------------------------------------------------------------------------------------------------------------------

# Добавление новых тестов

# Теперь мы знаем, что get_formatted_name() работает для простых имен, и мо-
# жем написать второй тест для имен из трех компонентов. Для этого в класс
# NamesTestCase добавляется еще один метод:

# import unittest
# from Testirovanie_chapter11 import get_formatted_name
#
#
# class NamesTestCase(unittest.TestCase):
#     """Тесты для 'Testirovanie_chapter11.py'."""
#
#     def test_first_last_name(self):
#         """Имена вида 'Janis Joplin' работают правильно?"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
#
#     def test_first_last_middle_name(self):
#         """Работают ли такие имена, как 'Wolfgang Amadeus Mozart ?'"""
#         formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')   # 1
#         self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
#
#
# if __name__ == '__main__':
#     unittest.main()


# Новому методу присваивается имя test_first_last_middle_name(). Имя метода
# должно начинаться с test_, чтобы этот метод выполнялся автоматически при запуске
# test_name_function.py. В остальном имя выбирается так, чтобы оно четко показывало,
# какое именно поведение get_formatted_name() мы тестируем. В результате при сбое
# теста вы сразу видите, к каким именам он относится. Не нужно опасаться длинных
# имен методов в классах TestCase: имена должны быть содержательными, чтобы до-
# нести информацию до разработчика в случае сбоя, а поскольку Python вызывает их
# автоматически, вам никогда не придется вручную вводить эти имена при вызове.
# Чтобы протестировать функцию, мы вызываем get_formatted_name() c тремя
# компонентами , после чего используем assertEqual() для проверки того, что
# возвращенное полное имя совпадает с ожидаемым. При повторном запуске test_
# name_function.py оба теста проходят успешно:

# Testing started at 13:25 ...
#
#
# Ran 2 tests in 0.002s
#
# OK

# Отлично! Теперь мы знаем, что функция по-прежнему работает с именами
# из двух компонентов, как Janis Joplin, но можем быть уверены в том, что она
# сработает и для имен с тремя компонентам — такими, как Wolfgang Amadeus
# Mozart.

# ---------------------------------------------------------------------------------------------------------------------

# УПРАЖНЕНИЯ

# 11-1. Город, страна: напишите функцию, которая получает два параметра: название
# страны и название города. Функция должна возвращать одну строку в формате «Го-
# род, Страна», например «Santiago, Chile». Сохраните функцию в модуле с именем city_
# functions.py.
# Создайте файл test_cities.py для тестирования только что написанной функции (не забудьте
# импортировать unittest и тестируемую функцию). Напишите метод test_city_country() для
# проверки того, что вызов функции с такими значениями, как ‘santiago’ и ‘chile’, дает пра-
# вильную строку. Запустите test_cities.py и убедитесь в том, что тест test_city_country() про-
# ходит успешно.

# def description_cities(country, city):
#     """Название страны и города"""
#     full_description = country + ' ' + city
#     return full_description.title()

# ---------------------------------------------------------------------------------------------------------------------

# 11-2. Население: измените свою функцию так, чтобы у нее был третий обязательный
# параметр — население. В новой версии функция должна возвращать одну строку вида
# «Santiago, Chile — population 5000000.» Снова запустите программу test_cities.py. Убедитесь
# в том, что тест test_city_country() на этот раз не проходит.
# Измените функцию так, чтобы параметр населения стал необязательным. Снова запустите
# test_cities.py и убедитесь в том, что тест test_city_country() проходит успешно.
# Напишите второй тест test_city_country_population(), который проверяет вызов функции
# со значениями ‘santiago’, ‘chile’ и ‘population=5000000’. Снова запустите test_cities.py и убе-
# дитесь в том, что новый тест проходит успешно.

# def description_cities(country, city, population=5000000):
#     """Название страны и города"""
#     if population:
#         full_description = country + ' ' + city + ' ' + str(population)
#     else:
#         full_description = country + ' ' + city
#     return full_description.title()


# ---------------------------------------------------------------------------------------------------------------------

# Тестирование класса

# В первой части этой главы мы писали тесты для отдельной функции. Сей-
# час мы займемся написанием тестов для класса. Классы будут использовать-
# ся во многих ваших программах, поэтому возможность доказать, что ваши
# классы
# работают правильно, будет безусловно полезной. Если тесты для класса,
# над которым
# вы работаете, проходят успешно, вы можете быть уверены в том,
# что усовершенствования класса не приведут к случайному нарушению его те-
# кущего поведения.

# Разные методы assert

# Класс unittest.TestCase содержит целое семейство проверочных методов assert.
# Как упоминалось ранее, эти методы проверяют, выполняется ли условие, которое
# должно выполняться в определенной точке вашего кода. Если условие истинно,
# как и предполагалось, то ваши ожидания относительно поведения части вашей
# программы подтверждаются; вы можете быть уверены в отсутствии ошибок. Если
# же условие, которое должно быть истинным, окажется ложным, то Python выдает
# исключение.
# В табл. 11.1 перечислены шесть часто используемых методов assert. С их помощью
# можно проверить, что возвращаемые значения равны или не равны ожидаемым,
# что значения равны True или False или что значения входят или не входят в за-
# данный список. Эти методы могут использоваться только в классах, наследующих
# от unittest.TestCase; рассмотрим пример использования такого метода в контексте
# тестирования реального класса.

# Таблица 11.1. Методы assert, предоставляемые модулем unittest

# Метод Использование
# assertEqual(a, b) Проверяет, что a == b
# assertNotEqual(a, b) Проверяет, что a != b
# assertTrue(x) Проверяет, что значение x истинно
# assertFalse(x) Проверяет, что значение x ложно
# assertIn(элемент, список) Проверяет, что элемент входит в список
# assertNotIn(элемент, список) Проверяет, что элемент не входит в список

# --------------------------------------------------------------------------------------------------------------------

# Класс для тестирования
#
# Тестирование класса имеет много общего с тестированием функции — значитель-
# ная часть работы направлена на тестирование поведения методов класса. Впрочем,
# существуют и различия, поэтому мы напишем отдельный класс для тестирования.
# Возьмем класс для управления проведением анонимных опросов:

