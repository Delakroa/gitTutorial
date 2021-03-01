# Эта глава посвящена функциям — именованным блокам кода, предназначенным
# для решения одной конкретной задачи. Чтобы выполнить задачу, определенную
# в виде функции, вы указываете имя функции, отвечающей за эту задачу. Если зада-
# ча должна многократно выполняться в программе, вам не придется заново вводить
# весь необходимый код; просто вызовите функцию, предназначенную для решения
# задачи, и этот вызов приказывает Python выполнить код, содержащийся внутри
# функции. Как вы вскоре убедитесь, использование функций упрощает чтение, на-
# писание, тестирование кода и исправление ошибок.
# В этой главе также рассматриваются возможности передачи информации функ-
# циям. Вы узнаете, как писать функции, основной задачей которых является вывод
# информации, и другие функции, предназначенные для обработки данных и возвра-
# щения значения (или набора значений.) Наконец, вы научитесь хранить функции
# в отдельных файлах, называемых модулями, для упорядочения файлов основной
# программы.

# ---------------------------------------------------------------------------------------------------------------------

# Определение функции

#  def greet_user():
#      """Выводит простое приветствие."""
#      print("Hello!")
#
#  greet_user()

# В этом примере представлена простейшая структура функции. Строка  при по-
# мощи ключевого слова def сообщает Python, что вы определяете функцию. В опре-
# делении функции указывается имя функции и, если нужно, описание информации,
# необходимой функции для решения ее задачи. Эта информация заключается
# в круглые скобки. В данном примере функции присвоено имя greet_user(), и она
# не нуждается в дополнительной информации для решения своей задачи, поэтому
# круглые скобки пусты. (Впрочем, даже в этом случае они обязательны.) Наконец,
# определение завершается двоеточием.
# Все строки с отступами, следующие за def greet_user():, образуют тело функ-
# ции. Текст в точке  представляет собой комментарий — строку документации
# 136 Глава 8 • Функции
# с описанием функции. Строки документации заключаются в утроенные кавычки;
# Python опознает их по этой последовательности символов во время генерирования
# документации к функциям в ваших программах.
# «Настоящий» код в теле этой функции состоит всего из одной строки
# print("Hello!") — см. . Таким образом, функция greet_user() решает всего
# одну задачу: выполнение команды print("Hello!").
# Когда потребуется использовать эту функцию, вызовите ее. Вызов функции при-
# казывает Python выполнить содержащийся в ней код. Чтобы вызвать функцию,
# укажите ее имя, за которым следует вся необходимая информация, заключенная
# в круглые скобки, как показано в строке . Так как никакая дополнительная ин-
# формация не нужна, вызов функции эквивалентен простому выполнению команды
# greet_user(). Как и ожидалось, функция выводит сообщение Hello!:

# -------------------------------------------------------------------------------------------------------------------

# Передача информации функции

# С небольшими изменениями функция greet_user() сможет не только сказать
# «Привет!» пользователю, но и поприветствовать его по имени. Для этого следует
# включить имя username в круглых скобках в определение функции def greet_
# user(). С добавлением username функция примет любое значение, которое будет
# заключено в скобки при вызове. Теперь функция ожидает, что при каждом вызове
# будет передаваться имя пользователя. При вызове greet_user() укажите имя (на-
# пример, 'jesse') в круглых скобках:

# def greet_user(username):
#     """Выводит простое приветствие."""
#     print("Helloy, " + username.title() + "!")

# greet_user('jesse')

# Команда greet_user('jesse') вызывает функцию greet_user() и передает ей
# информацию, необходимую для выполнения команды print. Функция получает
# переданное имя и выводит приветствие для этого имени:
# Hello, Jesse!
# Точно так же команда greet_user('sarah') вызывает функцию greet_user()
# и передает ей строку 'sarah', что приводит к выводу сообщения Hello, Sarah!
# Функцию greet_user() можно вызвать сколько угодно раз и передать ей любое
# имя на ваше усмотрение — и вы будете получать ожидаемый результат.

# --------------------------------------------------------------------------------------------------------------------

# Аргументы и параметры

# Функция greet_user() определена так, что для работы она должна получить
# значение переменной username. После того как функция будет вызвана и полу-
# чит необходимую информацию (имя пользователя), она выведет правильное
# приветствие.
# Передача аргументов 137
# Переменная username в определении greet_user() — параметр, то есть условные
# данные, необходимые функции для выполнения ее работы. Значение 'jesse'
# в greet_user('jesse') — аргумент, то есть конкретная информация, переданная
# при вызове функции. Вызывая функцию, вы заключаете значение, с которым
# функция должна работать, в круглые скобки. В данном случае аргумент 'jesse'
# был передан функции greet_user(), а его значение было сохранено в переменной
# username.

# -------------------------------------------------------------------------------------------------------------------

# УПРАЖНЕНИЯ
# 8-1. Сообщение: напишите функцию display_message() для вывода сообщения по теме, рас-
# сматриваемой в этой главе. Вызовите функцию и убедитесь в том, что сообщение выво-
# дится правильно.

# def display_massage(trening):
#     """Тренировка"""
#     print("Helloy World! " + trening.title())

# display_massage('dmitry')


# 8-2. Любимая книга: напишите функцию favorite_book(), которая получает один пара-
# метр title. Функция должна выводить сообщение вида «One of my favorite books is Alice in
# Wonderland». Вызовите функцию и убедитесь в том, что название книги правильно пере-
# дается как аргумент при вызове функции.

# def favorite_book(book):
#     """вывод любимой книги"""
#     print("Одна из любимых книг: " + book.title())

# favorite_book("туманность андромеды (ефремова)")

# ------------------------------------------------------------------------------------------------------------------

# Позиционные аргументы

# def describe_pet(animal_type, pet_name):
#     """Выводит информацию животного"""
#     print("\nУ меня есть " + animal_type + ".")
#     print("Моего " + animal_type + " зовут " + pet_name.title() + ".")

# describe_pet('хомяк', 'гарри')

# --------------------------------------------------------------------------------------------------------------------

# Многократный вызов функций

# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# --------------------------------------------------------------------------------------------------------------------

# Именованные аргументы

# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном."""

# print("\nI have a " + animal_type + ".")
# print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# describe_pet(animal_type='hamster', pet_name='harry')

# Функция describe_pet() не изменилась. Однако на этот раз при вызове функ-
# ции мы явно сообщаем Python, с каким параметром должен быть связан каждый
# аргумент. При обработке вызова функции Python знает, что аргумент 'hamster'
# должен быть сохранен в параметре animal_type, а аргумент 'harry' в параметре
# pet_name.
# Порядок следования именованных аргументов в данном случае не важен, потому
# что Python знает, где должно храниться каждое значение. Следующие два вызова
# функции эквивалентны:

# При использовании именованных аргументов будьте внимательны — имена должны точно совпа-
# дать с именами параметров из определения функции.

# -------------------------------------------------------------------------------------------------------------------

# Значения по умолчанию

# Для каждого параметра вашей функции можно определить значение по умолча-
# нию. Если при вызове функции передается аргумент, соответствующий данному
# параметру, Python использует значение аргумента, а если нет — использует зна-
# чение по умолчанию. Таким образом, если для параметра определено значение
# по умолчанию, вы можете опустить соответствующий аргумент, который обычно
# включается в вызов функции. Значения по умолчанию упрощают вызовы функций
# и проясняют типичные способы использования функций.
# Например, если вы заметили, что большинство вызовов describe_pet() исполь-
# зуется для описания собак, задайте animal_type значение по умолчанию 'dog'.
# Теперь в любом вызове describe_pet() для собаки эту информацию можно
# опустить:
# def describe_pet(pet_name, animal_type='dog'):
# """Выводит информацию о животном."""
# print("\nI have a " + animal_type + ".")
# print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet(pet_name='willie')

# Мы изменили определение describe_pet() и включили для параметра animal_type
# значение по умолчанию 'dog'. Если теперь функция будет вызвана без указания
# animal_type, Python знает, что для этого параметра следует использовать значение 'dog':
# I have a dog.
# My dog's name is Willie.

# ---------------------------------------------------------------------------------------------------------------------

# Эквивалентные вызовы функций

# Так как позиционные аргументы, именованные аргументы и значения по умол-
# чанию могут использоваться одновременно, часто существуют несколько эквива-
# лентных способов вызова функций. Возьмем оператор describe_pets() с одним
# значением по умолчанию:

# def describe_pet(pet_name, animal_type='dog'):

# При таком определении аргумент для параметра pet_name должен задаваться в любом случае, но это значение может
# передаваться как в позиционном, так и в име - нованном формате.Если описываемое животное не является собакой, то
# аргумент animal_type тоже должен быть включен в вызов, и этот аргумент тоже может быть задан как в позиционном, так
# и в именованном формате. Все следующие вызовы являются допустимыми для данной функции:

# describe_pet('willie')
# describe_pet(pet_name='willie')
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

# Все вызовы функции выдадут такой же результат, как и в предыдущих примерах.

# ПРИМЕЧАНИЕ
# На самом деле не так важно, какой стиль вызова вы используете. Если ваша функция выдает нуж-
# ный результат, выберите тот стиль, который вам кажется более понятным.

# --------------------------------------------------------------------------------------------------------------------

# УПРАЖНЕНИЯ
# 8-3. Футболка: напишите функцию make_shirt(), которая получает размер футболки и текст,
# который должен быть напечатан на ней. Функция должна выводить сообщение с размером
# и текстом. Вызовите функцию с использованием позиционных аргументов. Вызовите функ-
# цию во второй раз с использованием именованных аргументов.

# def make_shirt(size, text):
#     """описание футболки"""

# print('Размер моей футболки ' + size.title() + " с красивым текстом на ней " + text.title())


# make_shirt('xxl', 'hello world')


# def make_shirt(size, text):
#     """именованный агрумент"""
#     print('Размер моей футболки ' + size.title() + " с красивым текстом на ней " + text.title())


# make_shirt(size='XXL', text='hello world')


# --------------------------------------------------------------------------------------------------------------------

# 8-4. Большие футболки: измените функцию make_shirt(), чтобы футболки по умолчанию
# имели размер L, и на них выводился текст «I love Python.». Создайте футболку с размером
# L и текстом по умолчанию, а также футболку любого размера с другим текстом.

# def make_shirt(size, text):
#     """задание"""
#     print('Размер моей футболки ' + size.title() + ', с прикольным текстом на ней: ' + text.title())


# make_shirt(size='l', text='"i love python"')


# -------------------------------------------------------------------------------------------------------------------

# 8-5. Города: напишите функцию describe_city(), которая получает названия города и стра-
# ны. Функция должна выводить простое сообщение (например, «Reykjavik is in Iceland»). За-
# дайте параметру страны значение по умолчанию. Вызовите свою функцию для трех разных
# городов, по крайней мере один из которых не находится в стране по умолчанию.

# def discribe_city(city, country):
#     """описание города"""
#     print('Город ' + city.title() + ' находится в ' + country.title() + ';')


# discribe_city(city='тверь', country='россии')
# discribe_city(city='берлин', country='германии')
# discribe_city(city='рим', country='италии')

# -------------------------------------------------------------------------------------------------------------------

# Возвращаемое значение

# def get_formatted_name(first_name, last_name):  #1
    """Возвращает аккуратно отформатированныое имя."""
    # full_name = first_name + ' ' + last_name   #2
    # return full_name.title()  #3


# musician = get_formatted_name('jimi', 'hendrix')  #4
# print(musician)

# Определение get_formatted_name() получает в параметрах имя и фамилию .
# Функция объединяет эти два имени, добавляет между ними пробел и сохраняет
# результат в full_name . Значение full_name преобразуется в формат с начальной
# буквой верхнего регистра, а затем возвращается в точку вызова .
# Вызывая функцию, которая возвращает значение, необходимо предоставить пере-
# менную, в которой должно храниться возвращаемое значение. В данном случае
# возвращаемое значение сохраняется в переменной musician . Результат содержит
# аккуратно отформатированное полное имя, построенное из имени и фамилии:
# Jimi Hendrix
# Может показаться, что все эти хлопоты излишни — с таким же успехом можно
# было использовать команду:
# print("Jimi Hendrix")
# Но если представить, что вы пишете большую программу, в которой многочис-
# ленные имена и фамилии должны храниться по отдельности, такие функции, как
# get_formatted_name(), становятся чрезвычайно полезными. Вы храните имена
# отдельно от фамилий, а затем вызываете функцию везде, где потребуется вывести
# полное имя.

# --------------------------------------------------------------------------------------------------------------------

# Необязательные аргументы

