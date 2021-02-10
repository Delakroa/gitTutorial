# Нередко в программе требуется проверять более двух возможных ситуаций; для
# таких ситуаций в Python предусмотрен синтаксис if-elif-else. Python выполняет
# только один блок в цепочке if-elif-else. Все условия проверяются по порядку
# до тех пор, пока одно из них не даст истинный результат. Далее выполняется код,
# следующий за этим условием, а все остальные проверки Python пропускает.
# Во многих реальных ситуациях существуют более двух возможных результатов.
# Представьте себе парк аттракционов, который взимает разную плату за вход для
# разных возрастных групп:
# Для посетителей младше 4 лет вход бесплатный.
# Для посетителей от 4 до 18 лет билет стоит $5.
# Для посетителей от 18 лет и старше билет стоит $10.
# Как использовать команду if для определения платы за вход? Следующий код
# определяет, к какой возрастной категории относится посетитель, и выводит со-
# общение со стоимостью билета:

# age = 20
# if age < 4:
#     print('Для вас проход стоит 0$')
# elif age < 18:
#     print('Для вас сумма прохода составляет 5$')
# else:
#     print('Ваша цена составляет 10$')

# Вместо того чтобы выводить сообщение с ценой билета в блоках if-elif-else,
# лучше использовать другое, более компактное решение: присвоить цену в цепочке
# if-elif-else, а затем добавить одну команду print после выполнения цепочки:

# age = 18
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# else:
#     price = 10
# print('Стоимость вашего прохода $'+str(price) + '.')

# -----------------------------------------------------------------------------------------------------------

# Серии блоков elif
# Код может содержать сколько угодно блоков elif. Например, если парк аттракци-
# онов введет особую скидку для пожилых посетителей, вы можете добавить в свой
# Команды if 93
# код еще одну проверку для определения того, распространяется ли скидка на те-
# кущего посетителя. Допустим, посетители с возрастом 65 и выше платят половину
# от обычной цены билета, или $5:

# age = 66
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# else:
#     price = 5
# print('Стоимость вашего прохода составляет $' + str(price) + '.')

# -------------------------------------------------------------------------------------------------------------

# Отсутствие блока else
# Python не требует, чтобы цепочка if-elif непременно завершалась блоком else.
# Иногда блок else удобен; в других случаях бывает нагляднее использовать допол-
# нительную секцию elif для обработки конкретного условия:

# age = 65
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 65:
#     price = 5
# print('Стоимость вашего прохода составляет $' + str(price) + '.')


# Блок elif в точке  назначает цену $5, если возраст посетителя равен 65 и выше;
# смысл такого кода более понятен, чем у обобщенного блока else. С таким измене-
# нием выполнение каждого блока возможно только при истинности конкретного
# условия.
# Блок else «универсален»: он обрабатывает все условия, не подходящие ни под одну
# конкретную проверку if или elif, причем в эту категорию иногда могут попасть
# недействительные или даже вредоносные данные. Если у вас имеется завершающее
# конкретное условие, лучше используйте завершающий блок elif и опустите блок
# else. В этом случае вы можете быть уверены в том, что ваш код будет выполняться
# только в правильных условиях.


# -------------------------------------------------------------------------------------------------------

# Проверка нескольких условий

# Цепочки if-elif-else эффективны, но они подходят только в том случае, если ис-
# тинным должно быть только одно условие. Как только Python находит выполняющееся
# условие, все остальные проверки пропускаются. Такое поведение доста-
# точно эффективно, потому что оно позволяет проверить одно конкретное условие.
# Однако иногда бывает важно проверить все условия, представляющие интерес.
# В таких случаях следует применять серии простых команд if без блоков elif или
# else. Такое решение уместно, когда истинными могут быть сразу несколько усло-
# вий и вы хотите отреагировать на все истинные условия.
# Вернемся к примеру с пиццей. Если кто-то закажет пиццу с двумя дополнениями,
# программа должна обработать оба дополнения:

# requested_toppings = ['mushroom', 'extra cheese']
# if 'mushroom' in requested_toppings:
#     print('добавим грибы')
# if 'pepperoni' in requested_toppings:
#     print('добавим пепперони')
# if 'extra cheese' in requested_toppings:
#     print('добавим экстра сыр')
# print('\nПицца готова')

# -----------------------------------------------------------------------------------------------------------------

# Упражнение
# 5-3 Цвета 1: представьте, что в вашей компьютерной игре только что был подбит корабль
# пришельцев. Создайте переменную с именем alien_color и присвойте ей значение ‘green’,
# ‘yellow’ или ‘red’.
# • Напишите команду if для проверки того, что переменная содержит значение ‘green’.
# Если условие истинно, выведите сообщение о том, что игрок только что заработал
# 5 очков.
# • Напишите одну версию программы, в которой условие if выполняется, и другую вер-
# сию, в которой оно не выполняется. (Во второй версии никакое сообщение выводить-
# ся не должно.)

# alien_color = ['green', 'yellow', 'red']
# if 'green' in alien_color:
#     print('Вы заработали 5ять очков')
# else:
#     print('Вы проиграли')


# второй варинат

# alien_color = ['black', 'yellow', 'red']
# if 'green' in alien_color:
#     print('Вы заработали 5ять очков')

# 5-5. Цвета 3: преобразуйте цепочку if-else из упражнения 5-4 в цепочку if-elif-else.
# • Если переменная содержит значение 'green’, выведите сообщение о том, что игрок
# только что заработал 5 очков.
# • Если переменная содержит значение 'yellow’, выведите сообщение о том, что игрок
# только что заработал 10 очков.
# • Если переменная содержит значение 'red’, выведите сообщение о том, что игрок толь-
# ко что заработал 15 очков.
# • Напишите три версии программы и проследите за тем, чтобы для каждого цвета при-
# шельца выводилось соответствующее сообщение.
# alien_color = 'black'
# alien_color = 'green'
# alien_color = 'red'
# alien_color = 'yellow'
# if 'green' in alien_color:
#     print('Вы заработали 5ять очков')
# elif 'yellow' in alien_color:
#     print('Вы заработали 10 очков')
# elif 'red' in alien_color:
#     print('Вы заработали 15 очков')
# else:
#     print('Вы проиграли')

# alien_color = 'black'
# alien_color = 'green'
# alien_color = 'yellow'
# if 'green' in alien_color:
#     point = 5
# elif 'yellow' in alien_color:
#     point = 10
# elif 'red' in alien_color:
#     point = 15
# else:
#     print('Вы проиграли')
# print('Вы заработали ' + str(point) + ' очков.')


# 5-6. Периоды жизни: напишите цепочку if-elif-else для определения периода жизни челове-
# ка. Присвойте значение переменной age, а затем выведите сообщение.
# • Если значение меньше 2 — младенец.

# age = 100
# if age <= 2:
#     print('младенец')
# elif age <= 13:
#     print('ребёнок')
# elif age < 20:
#     print('подросток')
# elif age < 65:
#     print('взрослый')
# elif age >= 65:
#     print('пожилой человек')


# 5-7. Любимый фрукт: составьте список своих любимых фруктов. Напишите серию независи-
# мых команд if для проверки того, присутствуют ли некоторые фрукты в списке.
# • Создайте список трех своих любимых фруктов и назовите его favorite_fruits.
# • Напишите пять команд if. Каждая команда должна проверять, входит ли определен-
# ный тип фрукта в список. Если фрукт входит в список, блок if должен выводить со-
# общение вида «You really like bananas!».

# favorite_fruits = ['banana', 'orange', 'apple']
# if 'banana' in favorite_fruits:
#     print('Ты очень любишь бананы')
# if 'watermelon' in favorite_fruits:
#     print('Ты очень любишь арбуз')
# if 'apple' in favorite_fruits:
#     print('Ты очень любишь яблоки')
# if 'orange' in favorite_fruits:
#     print('Ты очень любишь апельсины')
# if 'coconut' in favorite_fruits:
#     print('Ты очень любишь кокос')

# -----------------------------------------------------------------------------------------------------------------

# requested_toppings = ['mushroom', 'green pepper', 'extra cheese']
# for requested_topping in requested_toppings:
#     print("добавим " + requested_topping + ".")
# print("\nПицца готова!")


# requested_toppings = ['mushroom', 'green pepper', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green pepper':
#         print('Извините но сейчас закончился зелёный перец.')
#     else:
#         print('Добавим ' + requested_topping + '.')
# print('\nПица готова')


# Проверка наличия элементов в списке
# Для всех списков, с которыми мы работали до сих пор, действовало одно про-
# стое предположение: мы считали, что в каждом списке есть хотя бы один эле-
# мент. Скоро мы предоставим пользователю возможность вводить информацию,
# хранящуюся в списке, поэтому мы уже не можем предполагать, что при каждом
# выполнении цикла в списке есть хотя бы один элемент. В такой ситуации перед
# выполнением цикла for будет полезно проверить, есть ли в списке хотя бы один
# элемент.
# Проверим, есть ли элементы в списке заказанных дополнений, перед изготовлением
# пиццы. Если список пуст, программа предлагает пользователю подтвердить, что он
# хочет базовую пиццу без дополнений. Если список не пуст, пицца готовится так
# же, как в предыдущих примерах:


# requested_toppings = []
# if requested_toppings:  # проверяет список
#     for requested_topping in requested_toppings:
#         print('Добавим ' + requested_topping + '.')
#         print('\nПица готова!')
# else:
#     print('Вы уверены, что хотите простую пиццу?')


# -----------------------------------------------------------------------------------------------------------------

# Множественные списки

# available_toppings = ['mushroom', 'olives', 'green pepper', 'pepperoni', 'pineapple', 'extra cheese']  # определяется доступный список продуктов к пице
# requested_toppings = ['mushroom', 'french fries', 'fish', 'extra cheese']   # запрошеная начинка
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print('добавим ' + requested_topping + ".")
#     else:
#         print('извините, у нас нет ' + requested_topping + ".")
# print('\nпица готова')


# ----------------------------------------------------------------------------------------------------------

# УПРАЖНЕНИЯ
# 5-8. Hello Admin: создайте список из пяти и более имен пользователей, включающий имя
# ‘admin’. Представьте, что вы пишете код, который выводит приветственное сообщение для
# каждого пользователя после его входа на сайт. Переберите элементы списка и выведите
# сообщение для каждого пользователя.
# • Для пользователя с именем 'admin’ выведите особое сообщение — например: «Hello
# admin, would you like to see a status report?»
# • В остальных случаях выводите универсальное приветствие — например: «Hello Eric,
# thank you for logging in again».

# users = ['Denis', 'Mark', 'Admin', 'Abraham', 'Oleg']
# for user in users:
#     if user == 'Admin':
#         print('Здравствуйте, админ, хотите увидеть отчет о состоянии?')
#     else:
#         print('Приветсвую вас на сайте ' + user + '.')


# 5-9. Без пользователей: добавьте в hello_admin.py команду if, которая проверит, что список
# пользователей не пуст.
# • Если список пуст, выведите сообщение: «We need to find some users!»
# • Удалите из списка все имена пользователей и убедитесь в том, что программа выво-
# дит правильное сообщение.

# users = []
# if users:
#     for user in users:
#         print('Приветствую вас ' + user + '.')
# else:
#     print('Нам необходимо найти пользователей!')


# 5-10. Проверка имен пользователей: выполните следующие действия для создания про-
# граммы, моделирующей проверку уникальности имен пользователей.
# • Создайте список current_users, содержащий пять и более имен пользователей.
# • Создайте другой список new_users, содержащий пять и более имен пользователей.
# Убедитесь в том, что одно или два новых имени также присутствуют в списке current_
# users.
# • Переберите список new_users и для каждого имени в этом списке проверьте, было ли
# оно использовано ранее. Если имя уже использовалось, выведите сообщение о том,
# что пользователь должен выбрать новое имя. Если имя не использовалось, выведите
# сообщение о его доступности.
# • Проследите за тем, чтобы сравнение выполнялось без учета регистра символов. Если
# имя 'John’ уже используется, в регистрации имени ‘JOHN’ следует отказать.
# стр. 99

current_users = ['Denis', 'Mark', 'Admin', 'Abraham', 'Oleg']
new_users = ['Denis', 'Mark', 'Alex', 'Oleg', 'Admin', 'Marina']
for new_user in new_users:
    if new_user in current_users:
        print('Необходимо выбрать новое имя ' + new_user + '.')
else:
    print('имя доступно ' + new_user + '.')
print('\nВы авторизованны ' + new_user + '.')


# разобратся почему не проходит имя Alex
