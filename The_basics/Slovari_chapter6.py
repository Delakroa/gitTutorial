# Возьмем игру с инопланетными пришельцами, которые имеют разные цвета и при-
# носят разное количество очков игроку. В следующем простом словаре хранится
# информация об одном конкретном пришельце:

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])


# Теперь программа может получить значение, связанное с любым из ключей
# в alien_0: color или points. Если игрок сбивает корабль пришельца, для получения
# заработанных им очков может использоваться код следующего вида:

# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print('Ты только что заработал ' + str(new_points) + ' points!')
# print('Ты только что заработал ' + str(alien_0['points']) + ' points') # мой варинат для понимания и закрепления

# -------------------------------------------------------------------------------------------------------------------

# Добавление новых пар "ключ - значение"

# Словари относятся к динамическим структурам данных: в словарь можно в любой
# момент добавлять новые пары «ключ—значение». Для этого указывается имя сло-
# варя, за которым в квадратных скобках следует новый ключ с новым значением.
# Добавим в словарь alien_0 еще два атрибута: координаты x и y для вывода изобра-
# жения пришельца в определенной позиции экрана. Допустим, пришелец должен
# отображаться у левого края экрана, в 25 пикселах от верхнего края. Так как система
# экранных координат обычно располагается в левом верхнем углу, для размещения
# пришельца у левого края координата x должна быть равна 0, а координата y — 25:

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# ---------------------------------------------------------------------------------------------------------------------

# Создание пустого словаря

# В некоторых ситуациях бывает удобно (или даже необходимо) начать с пустого
# словаря, а затем добавлять в него новые элементы. Чтобы начать заполнение пу-
# стого словаря, определите словарь с пустой парой фигурных скобок, а затем добав-
# ляйте новые пары «ключ—значение» (каждая пара в отдельной строке). Например,
# вот как строится словарь alien_0:

# alien_0 = {}
#
# alien_0['color'] = 'green'
# alien_0['points'] = 5
#
# print(alien_0)


# ------------------------------------------------------------------------------------------------------------------

# Изменение значений в словаре

# Чтобы изменить значение в словаре, укажите имя словаря с ключом в квадратных
# скобках, а затем новое значение, которое должно быть связано с этим ключом. До-
# пустим, в процессе игры цвет пришельца меняется с зеленого на желтый:

# alien_0 = {'color': 'green'}
# print("Пришелец сейчас " + alien_0['color'] + ".")
#
# alien_0['color'] = 'yelow'
# print('Пришелец сейчас ' + alien_0['color'] + '.')

# Ещё один пример поинтересней

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast', }
# print("Original x_position: " + str(alien_0['x_position']))
# Пришелец перемещается в право.
# Вычесляем величину смещения на основании текущей скорости.

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3  # Пришелец двигается быстро.
# alien_0['x_position'] = alien_0['x_position'] + x_increment  # Новая позиция равна сумме позиций иприращения.
# print("New x-position: " + str(alien_0['x_position']))

# ---------------------------------------------------------------------------------------------------------------------

# Удаление пар «ключ—значение»

# Когда информация, хранящаяся в словаре, перестает быть ненужной, пару «ключ—
# значение» можно полностью удалить при помощи команды del. При вызове до-
# статочно передать имя словаря и удаляемый ключ.
# Например, в следующем примере из словаря alien_0 удаляется ключ 'points'
# вместе со значением:

# alien_0 = {'color': 'green', 'point': 5}
# print(alien_0)
#
# del alien_0['point']
# print(alien_0)

# ---------------------------------------------------------------------------------------------------------------------

# Словарь с однотипным обьектами

# favorite_languages = {
#     'alex': 'python',
#     'den': 'c',
#     'andry': 'ruby',
#     'dimon': 'python',
# }
#
# print('dimon твой любимый язык программирования ' +
#       favorite_languages['dimon'].title() +
#       '.')
# ------------------------------------------------------------------------------------------------------------------

# 6-1. Человек: используйте словарь для сохранения информации об известном вам чело-
# веке. Сохраните имя, фамилию, возраст и город, в котором живет этот человек. Словарь
# должен содержать ключи с такими именами, как first_name, last_name, age и city. Выведите
# каждый фрагмент информации, хранящийся в словаре.


# passpor = {
#     'first_name': 'mitry',
#     'last_name': 'malikov',
#     'age': 1000,
#     'city': 'mukhosransk'
# }
#
# print(passpor)

# ------------------------------------------------------------------------------------------------------------------

# 6-2. Любимые числа: используйте словарь для хранения любимых чисел. Возьмите пять
# имен и используйте их как ключи словаря. Придумайте любимое число для каждого чело-
# века и сохраните его как значение в словаре. Выведите имя каждого человека и его люби-
# мое число. Чтобы задача стала более интересной, опросите нескольких друзей и соберите
# реальные данные для своей программы.

# razriadi = {
#     'slavik': 100,
#     'vova': 15,
#     'oleg': 7,
#     'alex': 1000,
#     'den': 0,
# }
# print(razriadi)


# 6-3. Глоссарий: словари Python могут использоваться для моделирования «настоящего»
# словаря (чтобы не создавать путаницы, назовем его «глоссарием»).
# • Вспомните пять терминов из области программирования, которые вы узнали
# в предыдущих главах. Используйте эти слова как ключи глоссария, а их определения — как
# значения.
# • Выведите каждое слово и его определение в аккуратно отформатированном виде.
# Например, вы можете вывести слово, затем двоеточие и определение; или же слово
# в одной строке, а его определение — с отступом в следующей строке. Используйте
# символ новой строки (\n) для вставки пустых строк между парами «слово-определе-
# ние» в выходных данных.

# golosary = {
#     "конкатэнация": "cложение",
#     "коммит": "сохранять скрин кода",
#     "пушить": "скидывать на свервер",
#     "пулить": "скачивать с сервера",
#     "итерация": "повторение",
# }
# for key, value in golosary.items():  # В данном примере показывается как вывести на экран все пары этой -
#     print(key, ":", value)  # коллекции в формате ключ : значение. Для этого используется цикл for и функция -
# items, работающая с элементами словаря.

# ------------------------------------------------------------------------------------------------------------

# ПЕРЕБОР СЛОВАРЯ:

# Словарь Python может содержать как несколько пар «ключ—значение», так и мил-
# лионы таких пар. Поскольку в словаре может храниться большой объем данных,
# Python предоставляет средства для перебора элементов словаря. Информация
# может храниться в словарях по-разному, поэтому предусмотрены разные способы
# перебора. Программа может перебрать все пары «ключ—значение» в словаре, толь-
# ко ключи или только значения.

# Перебор всех пар «ключ—значение»

# user_0 = {
#     "username": "efermi",
#     "firstname": "enrico",
#     "last": "fermi",
# }
# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value " + value)
#     print(key, ":", value)

# Ещё один пример:

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# for name, language in favorite_languages.items():
#     print(name.title() + " любимый язык " + language.title() + ".")

# ------------------------------------------------------------------------------------------------------------------

# Перебор всех ключей в словаре:

# Метод keys() удобен в тех случаях, когда вы не собираетесь работать со всеми
# значениями в словаре. Переберем словарь favorite_languages и выведем имена
# всех людей, участвовавших в опросе:

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name in favorite_languages.keys():  # На самом деле перебор ключей используется по умолчанию при переборе
#     print(name.title())                 # словаря,так что этот код будет работать точно так же,
# как если бы вы написали for name in favorite_languages:


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(" Хай " + name.title() + ", я вижу твой любимый язык " + favorite_languages[name].title() + "!")

# Метод keys() также может использоваться для проверки того, участвовал ли кон-
# кретный человек в опросе:

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# if 'erin' not in favorite_languages.keys():  # строка 
#     print("Erin, пожалуйста примите участие в нашем опросе!")
# Метод keys() не ограничивается перебором: он возвращает список всех ключей,
# и строка  просто проверяет, входит ли ключ 'erin' в список. Так как ключ в спи-
# ске отсутствует, программа выводит сообщение:
# Erin, please take our poll!

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name in sorted(favorite_languages.keys()):   # sorted выстраивает в алфовитном порядке
#     print(name.title() + ", спасибо что учавствовали в опросе.")
#
# Эта команда for не отличается от других команд for, если не считать того, что
# метод dictionary.keys() заключен в вызов функции sorted(). Эта конструкция
# приказывает Python выдать список всех ключей в словаре и отсортировать его
# перед тем, как перебирать элементы. В выводе перечислены все пользователи,
# участвовавшие в опросе, а их имена упорядочены по алфавиту:

# ---------------------------------------------------------------------------------------------------------------------

# Перебор всех значений в словаре

# Если вас прежде всего интересуют значения, содержащиеся в словаре, используйте
# метод values() для получения списка значений без ключей. Допустим, вы хотите
# просто получить список всех языков, выбранных в опросе, и вас не интересуют
# имена людей, выбравших каждый язык:

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
#
# print("Были упомянуты следующие языки:")
# for language in favorite_languages.values():
#     print(language.title())

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# print("Были упомянуты следующие языки:")
# for languages in set(favorite_languages.values()):   # set убирает множество (повторения), в нашем случае python
#     print(languages.title())

# Когда список, содержащий дубликаты, заключается в вызов set(), Python находит
# уникальные элементы списка и строит множество из этих элементов. В точке 
# set() используется для извлечения уникальных языков из favorite_languages.
# values(). В результате создается не содержащий дубликатов список языков про-
# граммирования, упомянутых участниками опроса:

# ---------------------------------------------------------------------------------------------------------------

# 6-4. Глоссарий 2: теперь, когда вы знаете, как перебрать элементы словаря, упростите код
# из упражнения 6-3, заменив серию команд print циклом, перебирающим ключи и значения
# словаря. Когда вы будете уверены в том, что цикл работает, добавьте в глоссарий еще пять
# терминов Python. При повторном запуске программы новые слова и значения должны быть
# автоматически включены в вывод.

# golosary = {
#     "конкатэнация": "cложение",
#     "коммит": "сохранять скрин кода",
#     "пушить": "скидывать на свервер",
#     "пулить": "скачивать с сервера",
#     "итерация": "повторение",
# }
# golosary['string'] = 'строка'
# golosary['len'] = 'кол-во символов'
# golosary['integer'] = 'целое число'
# golosary['slices'] = 'срезы'
#
# for key, value in golosary.items():
#     print(key, ":", value)

# ---------------------------------------------------------------------------------------------------------------------

# 6-5. Реки: создайте словарь с тремя большими реками и странами, по которым протекает
# каждая река. Одна из возможных пар «ключ—значение» — ‘nile’: ‘egypt’.
# • Используйте цикл для вывода сообщения с упоминанием реки и страны — например,
# «The Nile runs through Egypt.»
# • Используйте цикл для вывода названия каждой реки, включенной в словарь.
# • Используйте цикл для вывода названия каждой страны, включенной в слова

# rivers = {
#     'nile': 'egipt',
#     'volga': 'moscow',
#     'amazon': 'south america',
# }
# for key, value in rivers.items():
#     print(key.title() + ":" + ' протекает через ' + value.title() + ".")

# 6-6. Опрос: Возьмите за основу код favorite_languages.py (с. 106).
# • Создайте список людей, которые должны участвовать в опросе по поводу любимо-
# го языка программирования. Включите некоторые имена, которые уже присутствуют
# в списке, и некоторые имена, которых в списке еще нет.
# • Переберите список людей, которые должны участвовать в опросе. Если они уже прош-
# ли опрос, выведите сообщение с благодарностью за участие. Если они еще не про-
# ходили опрос, выведите сообщение с предложением принять участие.


# favorite_languages = ['jen', 'sarah', 'edward', 'phil']
# list_of_names = ['dmitry', 'volodia', 'oleg', 'denchik']
# for favorite_language in favorite_languages:
#     if favorite_language:
#         print('спасибо за участие ' + favorite_language.title() + '.')
# else:
#     for list_of_name in list_of_names:  # никогда так не делал, не знаю правилно ли
#         print('не хотели бы вы принять участие ' + str(list_of_name) + '.')

# ХЗ ПРАВИЛЬНО ЛИ. ВЫГЛЯДИТ СТРАННО, НО РАБОТАЕТ. ПОЧЕМУ ТАК, ДА ПОТОМУ ЧТО ДРУГИХ НАВАРОЧЕННЫХ МЕТОДОВ Я ЕЩЁ НЕ ЗНАЮ
# ДЕЛАЮ ИЗ ТОГО ЧТО ЕСТЬ. НУЖНО ПРОКОНСУЛЬТИРОВАТЬСЯ У СПЕЦОВ.

# -----------------------------------------------------------------------------------------------------------------

# Вложение:

# Иногда нужно сохранить множество словарей в списке или сохранить спи-
# сок как значение элемента словаря. Создание сложных структур такого рода
# называется
# вложением. Вы можете вложить множество словарей в список,
# список элементов в словарь или даже словарь внутрь другого словаря. Как
# наглядно
# показывают следующие примеры, вложение — чрезвычайно мощный
# механизм.


# Словарь alien_0 содержит разнообразную информацию об одном пришельце, но
# в нем нет места для хранения информации о втором пришельце, не говоря уже
# о целом экране, забитом пришельцами. Как смоделировать флот вторжения? На-
# пример, можно создать список пришельцев, в котором каждый элемент представ-
# ляет собой словарь с информацией о пришельце. Следующий код строит список
# из трех пришельцев:

# alien_0 = {'color': 'green', 'point': 5}
# alien_1 = {'color': 'yellow', 'point': 10}
# alien_2 = {'color': 'red', 'point': 15}

# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# Сначала создаются три словаря, каждый из которых представляет отдельного при-
# шельца. В точке  каждый словарь заносится в список с именем aliens. Наконец,
# программа перебирает список и выводит каждого пришельца:

# -------------------------------------------------------------------------------------------------------

# Конечно, в реалистичном примере будут использоваться более трех пришельцев,
# которые будут генерироваться автоматически. В следующем примере функция
# range() создает флот из 30 пришельцев:

# aliens = []  # создадим пустой список для хранения пришелцев.
# for alien_number in range(30):  # создадим 30 зелёных пришельцев.
#     new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:  # вывод 5яти пришельцев.
#     print(alien)
# print("...")

# print("полное число пришельцев " + str(len(aliens)))  # Вывод кол-ва созданых пришельцев.


# В начале примера список для хранения всех пришельцев, которые будут созданы,
# пуст. В точке  функция range() возвращает множество чисел, которое просто
# сообщает Python, сколько раз должен повторяться цикл. При каждом выполнении
# цикла создается новый пришелец , который затем добавляется в список aliens .
# В точке  срез используется для вывода первых пяти пришельцев, а в точке 
# выводится длина списка (для демонстрации того, что программа действительно
# сгенерировала весь флот из 30 пришельцев):

# aliens = []
# for vrem_alien in range(30):
#     new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[3:6]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow',
#         alien['speed'] = 'medium',
#         alien['point'] = 10
#     elif alien['color'] == 'yellow':  # не понятно почему не заменяется на красный?
#         alien['color'] = 'red',
#         alien['speed'] = 'fast',
#         alien['point'] = 15
# for alien in aliens[0:11]:
#     print(alien)
# print("...")
# print('\nобщее \nколичество \nпришельцев \n' + str(len(aliens)))

# --------------------------------------------------------------------------------------------------------------------

# СПИСОК В СЛОВАРЕ:

# pizza = {  # сохраним информацию о заказе
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# print('вы заказали ' + pizza['crust'] + '-crust pizza ' + 'со следующими начинками:')  # Описание заказа.
# for topping in pizza['toppings']:
#     print('\t' + topping)


# Вложение списка в словарь может применяться каждый раз, когда с одним ключом
# словаря должно быть связано более одного значения. Если бы в предыдущем при-
# мере с языками программирования ответы сохранялись в списке, один участник
# опроса мог бы выбрать сразу несколько любимых языков. При переборе словаря
# значение, связанное с каждым человеком, представляло бы собой список языков
# (вместо одного языка.) В цикле for словаря создается другой цикл для перебора
# списка языков, связанных с каждым участником:

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }
# for name, languages in favorite_languages.items():  # 
#     print("\n" + name.title() + " любимые языки:")
#     for language in languages:  # 
#         print("\t" + language.title())

# Вы видите в точке , что значение, связанное с каждым именем, теперь представ-
# ляет собой список. У некоторых участников только один любимый язык програм-
# мирования, у других таких языков несколько. При переборе словаря в точке 
# переменная с именем languages используется для хранения каждого значения
# из словаря, потому что мы знаем, что каждое значение будет представлять собой
# список. В основном цикле по элементам словаря другой цикл  перебирает эле-
# менты списка любимых языков каждого участника.
# Теперь каждый участник опроса может указать сколько угодно любимых языков
# программирования.


# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python'],
#
# }
# for name, languages in favorite_languages.items():   # мой варинат
#
#     if len(languages) != 2:
#         print(name.title() + ' единственный любимый язык:\n\t' + str(languages).title())
#     else:
#         print("\n" + name.title() + " любимые языки:\n\t" + str(languages).title())

# ----------------------------------------------------------------------------------------------------------------

# Словарь в словаре:

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }
#
# for username, user_info in users.items():
#     print("\nИмя пользователя " + username)
#     full_name = user_info['first'] + " " + user_info['last']
#     loction = user_info['location']
#     print("\tПолное имя: " + full_name.title())
#     print("\tМесто расположения " + loction.title())


# В программе определяется словарь с именем users, содержащий два ключа: для
# пользователей 'aeinstein' и 'mcurie'. Значение, связанное с каждым ключом,
# представляет собой словарь с именем, фамилией и местом жительства пользова-
# теля. В процессе перебора словаря users в точке  Python сохраняет каждый ключ
# в переменной username, а словарь, связанный с каждым именем пользователя, со-
# храняется в переменной user_info. Внутри основного цикла в словаре выводится
# имя пользователя .
# В точке  начинается работа с внутренним словарем. Переменная user_info, со-
# держащая словарь с информацией о пользователе, содержит три ключа: 'first',
# 'last' и 'location'. Каждый ключ используется для построения аккуратно от-
# форматированных данных с полным именем и местом жительства пользователя,
# с последующим выводом сводки известной информации о пользователе :

# ----------------------------------------------------------------------------------------------------------------

# 6-7. Люди: начните с программы, написанной для упражнения 6-1 (с. 107). Создайте два
# новых словаря, представляющих разных людей, и сохраните все три словаря в списке
# с именем people. Переберите элементы списка людей. В процессе перебора выведите всю
# имеющуюся информацию о каждом человеке.

# people = {
#     'vova': {
#         'имя': 'владимер',
#         'фамилия': 'рахманов',
#         'проживание': 'черногубовой',
#     },
#     'slava': {
#         'имя': 'Вячеслав',
#         'фамилия': 'баусов',
#         'проживание': 'без определенного'
#     },
#     'oleg': {
#         'имя': 'олег',
#         'фамилия': 'евсеев',
#         'проживание': 'тверь',
#     }
# }
# for username, user_info in people.items():
#     print('\nВаше имя ' + username.title())
#     full_name = user_info['имя'] + ' ' + user_info['фамилия']
#     location = user_info['проживание']
#     print('\tПолное имя: ' + full_name.title())
#     print('\tПроживание: ' + location.title())

# --------------------------------------------------------------------------------------------------------------------

# 6-8. Домашние животные: создайте несколько словарей, имена которых представляют
# клички домашних животных. В каждом словаре сохраните информацию о виде животно-
# го и имени владельца. Сохраните словари в списке с именем pets. Переберите элементы
# списка. В процессе перебора выведите всю имеющуюся информацию о каждом животном.

# pets = {
#     "lucky": {
#         "вид животного": "собака",
#         "имя владельца": "николай",
#     },
#     "gosha": {
#         "вид животного": "попугай",
#         "имя владельца": "дмитрий",
#     },
#     "murzik": {
#         "вид животного": "кот",
#         "имя владельца": "толик",
#     },
# }
# for name_pets, name_owner in pets.items():
#     print('\nКличка животного: ' + name_pets.title())
#     print('Вид животного: ' + name_owner['вид животного'].title() + '\nВладелец зверюги: ' +
#           name_owner['имя владельца'].title())

# ------------------------------------------------------------------------------------------------------------------

# 6-9. Любимые места: создайте словарь с именем favorite_places. Придумайте названия трех
# мест, которые станут ключами словаря, и сохраните для каждого человека от одного до
# трех любимых мест. Чтобы задача стала более интересной, опросите нескольких друзей
# и соберите реальные данные для своей программы. Переберите данные в словаре, выведи-
# те имя каждого человека и его любимые места.

# favorite_places = {
#     'селиегер': {
#         'имя': 'володя',
#         'фамилия': 'рахманов',
#         'любимое место': ['кровать', 'лесное', 'крым'],
#     },
#     'медведица': {
#         'имя': 'олег',
#         'фамилия': 'евсеев',
#         'любимое место': ['массажная', 'столовая', 'аптека'],
#     },
#     'карелия': {
#         'имя': 'славик',
#         'фамилия': 'баусмэн',
#         'любимое место': ['столовая', 'туалет', 'торжок'],
#     },
# }
# for favorite_place, discription in favorite_places.items():
#     names = discription['имя'] + ' ' + discription['фамилия']
#     print("\nданные друзей: " + names.title())
#     print("любимое место: " + str(discription['любимое место']))

# --------------------------------------------------------------------------------------------------------------------

# 6-10. Любимые числа: измените программу из упражнения 6-2 (с. 107), чтобы для каждого
# человека можно было хранить более одного любимого числа. Выведите имя каждого чело-
# века в списке и его любимые числа.

# razriadi = {
#     'slavik': [100, 5, 20],
#     'vova': [15, 54, 564],
#     'oleg': [7, 100500, 99],
#     'alex': [1000, 654, 66],
#     'den': [0, 8489, 58],
# }
# for name, value in razriadi.items():
#     print("Имя: " + name.title() + "\n" + "Любимые числа:\n " + str(value) + "\n")

# ---------------------------------------------------------------------------------------------------------------------

# 6-11. Города: создайте словарь с именем cities. Используйте названия трех городов в каче-
# стве ключей словаря. Создайте словарь с информацией о каждом городе; включите в него
# страну, в которой расположен город, примерную численность населения и один примеча-
# тельный факт, относящийся к этому городу. Ключи словаря каждого города должны на-
# зываться country, population и fact. Выведите название каждого города и всю сохраненную
# информацию о нем.

# cities = {
#     "tver": {
#         "country": "россия",
#         "population": "408 000",
#         "fact": "шансонье Михаил Круг",
#     },
#     "berlin": {
#         "country": "германия",
#         "population": "3 769 000",
#         "fact": "один из самых популярных городов европы",
#     },
#     "toronto": {
#         "country": "канада",
#         "population": "2 930 000",
#         "fact": "внесён в книгу рекордов Гиннесса как город с самой протяжённой системой подземных пешеходных тоннелей",
#     },
# }
# for citi, description in cities.items():
#     print("\t" + "Город: " + citi.title())
#     print("\tСтрана: " + description['country'].title() + "\n\t" + "Население: " + description['population']
#           + "\n\t" + "Некоторые факты о городе: " + description['fact'] + "\n")


# -------------------------------------------------------------------------------------------------------------------

# 6-12. Расширение: примеры, с которыми мы работаем, стали достаточно сложными, и в них
# можно вносить разного рода усовершенствования. Воспользуйтесь одним из примеров этой
# главы и расширьте его: добавьте новые ключи и значения, измените контекст программы
# или улучшите форматирование вывода.

#  Я уже со всем этим извращался ----> идём дальше

# --------------------------------------------------------------------------------------------------------------------

# c помощью команды update мы обьединяем два списка вместе

# names = {
#     'dmitry': 'khalikov',
#     'vova': 'rakhmanov',
#     'oleg': 'evseev',
# }

# new_names = {
#     'alex': 'latishev',
#     'nikola': 'novotorcev',
# }

# names.update(new_names)

# print(names)