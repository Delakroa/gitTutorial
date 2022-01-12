# ПРОСТОЙ ПРИМЕР:
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())  # команда upper делает обьек большими буквами
#     else:
#         print(car.title())

# -------------------------------------------------------------------------------------------------------------
#  ПРОВЕРКА УСЛОВИЯ:
# В каждой команде if центральное место занимает выражение, результатом которо-
# го является логическая истина (True) или логическая ложь (False); это выражение
# называется условием. В зависимости от результата проверки Python решает, должен
# ли выполняться код в команде if. Если результат условия равен True, то Python
# выполняет код, следующий за командой if.

# ПРОВЕРКА РАВЕНСТВА:
# Во многих условиях текущее значение переменной сравнивается с конкретным
# значением, интересующим вас. Простейшее условие проверяет, равно ли значение
# переменной конкретной величине:
#  >>> car = 'bmw'
#  >>> car == 'bmw'
# True
# В строке  переменной car присваивается значение 'bmw'; операция выполняется
# одним знаком =, как вы уже неоднократно видели. Строка  проверяет, равно ли
# значение car строке 'bmw'; для проверки используется двойной знак равенства (==).
# Этот оператор возвращает True, если значения слева и справа от оператора равны;
# если же значения не совпадают, оператор возвращает False. В нашем примере
# значения совпадают, поэтому Python возвращает True.
# Если car принимает любое другое значение вместо 'bmw', проверка возвращает
# False:
#  >>> car = 'audi'
#  >>> car == 'bmw'
# False
# Одиночный знак равенства выполняет операцию; код  можно прочитать в форме
# «Присвоить car значение 'audi'». С другой стороны, двойной знак равенства, как
# в строке , задает вопрос: «Значение car равно 'bmw'?» Такое применение знаков
# равенства встречается во многих языках программирования.


# ПРОВЕРКА РАВЕНСТВА БЕЗ УЧЁТА РЕГИСТРА:
# В языке Python проверка равенства выполняется с учетом регистра. Например, два
# значения с разным регистром символов равными не считаются:

# >>> car = 'Audi'
# >>> car == 'audi'
# False

# Если регистр символов важен, такое поведение приносит пользу. Но если проверка
# должна выполняться на уровне символов без учета регистра, преобразуйте значение
# переменной к нижнему регистру перед выполнением сравнения:

# >>> car = 'Audi'
# >>> car.lower() == 'audi'
# True

# Условие возвращает True независимо от регистра символов 'Audi', потому что
# проверка теперь выполняется без учета регистра. Функция lower() не изменяет
# значения, которое изначально хранилось в car, так что сравнение не отражается
# на исходной переменной:

# -------------------------------------------------------------------------------------------------------------------

# ПРОВЕРКА НЕРАВЕСТВА:

# requested_topping = 'mushroom'
#
# if requested_topping != 'anchovies':
#     print("Hold the anchovies")
# else:
#     print('sosi bibu')

# ---------------------------------------------------------------------------------------------------------------

# СРАВНИВАНИЯ ЧИСЕЛ:

# answer = 17
# if answer != 42:
#     print('это верный ответ')
# else:
#     print('это не корректный ответ, попробуйте ещё раз')
# -------------------------------------------------------------------------------------------------------------
# ПРОВЕРКА НЕСКОЛЬКИХ УСЛОВИЙ:
# Использование and для проверки нескольких условий

# Чтобы проверить, что два условия истинны одновременно, объедините их ключевым
# словом and; если оба условия истинны, то и все выражение тоже истинно. Если хотя
# бы одно (или оба) условия ложны, то и результат всего выражения равен False.
# Например, чтобы убедиться в том, что каждому из двух людей больше 21 года, ис-
# пользуйте следующую проверку:

#  >>> age_0 = 22
# >>> age_1 = 18
#  >>> age_0 >= 21 and age_1 >= 21
# False
#  >>> age_1 = 22
# >>> age_0 >= 21 and age_1 >= 21
# True

# -------------------------------------------------------------------------------------------------

# Использование or для проверки нескольких условий:

# Ключевое слово or тоже позволяет проверить несколько условий, но результат
# общей проверки является истинным в том случае, когда истинно хотя бы одно
# или оба условия. Ложный результат достигается только в том случае, если оба от-
# дельных условия ложны.
# Вернемся к примеру с возрастом, но на этот раз проверим, что хотя бы одна из двух
# переменных больше 21:

#  >>> age_0 = 22
# >>> age_1 = 18
#  >>> age_0 >= 21 or age_1 >= 21
# True
#  >>> age_0 = 18
# >>> age_0 >= 21 or age_1 >= 21
# False

# -----------------------------------------------------------------------------------------------------------------

# Проверка отсутствия значения в списке: (стр.88)
# В других случаях программа должна убедиться в том, что значение не входит
# в список. Для этого используется ключевое слово not. Для примера рассмотрим
# список пользователей, которым запрещено писать комментарии на форуме. Прежде
# чем разрешить пользователю отправку комментария, можно проверить, не был ли
# пользователь включен в «черный список»:

# banned_user = ['andrew', 'carolina', 'david']
# user = 'marie'
#
# if user not in banned_user:  # Для этого используется ключевое слово not.
#     print(user.title() + ", вы можете опубликовать ответ, если хотите.")

# -----------------------------------------------------------------------------------------------------------

# Логические выражения:

# В процессе изучения программирования вы рано или поздно услышите термин
# «логическое выражение». По сути это всего лишь другое название для проверки
# условия. Результат логического выражения равен True или False, как и результат
# условного выражения после его вычисления.
# Логические выражения часто используются для проверки некоторых условий —
# например, запущена ли компьютерная игра или разрешено ли пользователю редак-
# тирование некоторой информации на сайте:
# game_active = True
# can_edit = False
# Логические выражения предоставляют эффективные средства для контроля со-
# стояния программы или определенного условия, играющего важную роль в вашей
# программе.

# ------------------------------------------------------------------------------------------------------------

