# Как работает функция input()

# Функция input() приостанавливает выполнение программы и ожидает, пока
# пользователь введет некоторый текст. Получив ввод, Python сохраняет его в пере-
# менной, чтобы вам было удобнее работать с ним.
# Например, следующая программа предлагает пользователю ввести текст, а затем
# выводит сообщение для пользователя:

# messege = input("Скажи мне что нибудь и я это повторю вам: ")
# print(messege)

# --------------------------------------------------------------------------------------------------------------------

# Содержательные подсказки

# Каждый раз, когда в вашей программе используется функция input(), вы должны
# включать четкую, понятную подсказку, которая точно сообщит пользователю,
# какую информацию вы от него хотите получить. Подойдет любое предложение,
# которое сообщает пользователю, что нужно вводить. Пример:

# name = input("Пожадуйста введите ваше имя: ")
# print("Привет, " + name.title() + "!")


# promt = "Если вы сообщите нам, кто вы, мы сможем персонализировать сообщения, которое вы видите."
# promt += "\nКак тебя зовут? "  # оператор += обьединяет текст хранящийся в переменной prompt
#
# name = input(promt)
# print("\nПривет, " + name + "!")

# -----------------------------------------------------------------------------------------------------------------

# Использование int() для получения числового ввода:

# height = input("Какой у вас рост в дюймах? ")
# height = int(height)
# if height >= 36:
#     print("\nВы достаточно высоки, чтобы ездить верхом!")
# else:
#     print("\nВы сможете ездить верхом, когда станете немного старше. ")

# Если пользователь вводит числовые данные, которые используются в вашей про-
# грамме для вычислений и сравнений, обязательно преобразуйте введенное значение
# в его числовой эквивалент.

# ----------------------------------------------------------------------------------------------------------------------

# При работе с числовыми данными может пригодиться оператор вычисления остат-
# ка (%), который делит одно число на другое и возвращает остаток:

# Оператор % не сообщает частное от целочисленного деления; он возвращает только
# остаток.
# Когда одно число нацело делится на другое, остаток равен 0, и оператор % возвра-
# щает 0. Например, этот факт может использоваться для проверки четности или
# нечетности числа:

# number = input("Введите число, и я скажу его чётное или нечётное: ")
# number = int(number)
#
# if number % 2 == 0:
#     print("\nНомер " + str(number) + " чётное.")
# else:
#     print("\nНомер " + str(number) + " нечётный.")

# ---------------------------------------------------------------------------------------------------------------------

# 7-1. Прокат машин: напишите программу, которая спрашивает у пользователя, какую ма-
# шину он хотел бы взять напрокат. Выведите сообщение с введенными данными (например,
# “Дай мне посмотреть, найду ли я тебе Субару”).

# cars = input("какую машину вы хотели бы взять напрокат? ")
# print("\nДай мне посмотреть, найду ли я тебе " + cars)

# --------------------------------------------------------------------------------------------------------------------

# 7-2. Заказ стола: напишите программу, которая спрашивает у пользователя, на сколько
# мест он хочет забронировать стол в ресторане. Если введенное число больше 8, выведите
# сообщение о том, что пользователю придется подождать. В противном случае сообщите,
# что стол готов.

# book_your_place = input("На какое сколько мест вы хотите забронировать стол в ресторане: ")
# book_your_place = int(book_your_place)
# if book_your_place > 8:
#     print("Извините, но вам придётся подождать ")
# else:
#     print("Столы свободны ")

# -------------------------------------------------------------------------------------------------------------------

# 7-3. Числа, кратные 10: запросите у пользователя число и сообщите, кратно оно 10 или нет.

# numbers = input("Введите число: ")
# numbers = int(numbers)
#
# if numbers % 10 == 0:
#     print("Число кратное")
# else:
#     print("Число не кратное")

# -------------------------------------------------------------------------------------------------------------------

# Циклы while
#
# Цикл for получает коллекцию элементов и выполняет блок кода по одному разу
# для каждого элемента в коллекции. В отличие от него, цикл while продолжает вы-
# полняться, пока остается истинным некоторое условие.

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# В первой строке отсчет начинается с 1, для чего current_number присваивается
# значение 1. Далее запускается цикл while, который продолжает работать, пока
# значение current_number остается меньшим или равным 5. Код в цикле выводит
# значение current_number и увеличивает его на 1 командой current_number += 1.
# (Оператор += является сокращенной формой записи для current_number =
# current_number + 1.)
# Цикл повторяется, пока условие current_number <= 5 остается истинным. Так как
# 1 меньше 5, Python выводит 1, а затем увеличивает значение на 1, отчего current_
# number становится равным 2. Так как 2 меньше 5, Python выводит 2 и снова при-
# бавляет 1 и т. д. Как только значение current_number превысит 5, цикл останавли-
# вается, а программа завершается:

# --------------------------------------------------------------------------------------------------------------------

# Пользователь решает прервать работу программы

# prompt = "\nСкажи мне что-нибудь, и я тебе отвечу: "  # В точке  определяется сообщение, которое объясняет,
# prompt += "\nВведи 'quit' чтоб завершить программу. "  # что у пользователя есть два варианта:
# message = ""  # Затем переменной message  присваивается значение, введенное пользователем
# while message != 'quit':  # Цикл while  выполняется, пока значение message не равно 'quit'.
#     message = input(prompt)  # При выполнении команды message = input(prompt) Python отображает
#     print(message)

# При выполнении команды message = input(prompt) Python отображает
# подсказку и ожидает, пока пользователь введет данные. Эти данные сохраняются
# в message и выводятся командой print; после этого Python снова проверяет усло-
# вие команды while. Пока пользователь не введет слово 'quit', приглашение будет
# 126 Глава 7 • Ввод данных и циклы while
# выводиться снова и снова, а Python будет ожидать новых данных. При вводе слова
# 'quit' Python перестает выполнять цикл while, а программа завершается:

# ----------------------------------------------------------------------------------------------------------------------

# prompt = "\nСкажи мне что-нибудь, и я тебе отвечу: "
# prompt += "\nВведи 'quit' чтоб завершить программу. "
# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
#
#
# Теперь программа проводит проверку перед выводом сообщения и выводит со-
# общение только в том случае, если оно не совпадает с признаком завершения:

# -------------------------------------------------------------------------------------------------------------------

# ФЛАГИ

# В предыдущем примере программа выполняла некоторые операции, пока заданное
# условие оставалось истинным. А что если вы пишете более сложную программу,
# выполнение которой может прерываться по нескольким разным условиям?
# Например, компьютерная игра может завершаться по разным причинам: у игро-
# ка кончились все «жизни»; прошло отведенное время; все города, которые он
# должен был защищать, были уничтожены и т. д. Игра должна завершаться
# при выполнении любого из этих условий. Попытки проверять все возможные
# условия в одной команде while быстро усложняются и становятся слишком
# громоздкими.

# Если программа должна выполняться только при истинности нескольких условий,
# определите одну переменную-флаг. Эта переменная сообщает, должна ли програм-
# ма выполняться далее. Программу можно написать так, чтобы она продолжала
# выполнение, если флаг находится в состоянии True, и завершалась, если любое
# из нескольких событий перевело флаг в состояние False. В результате в команде
# while достаточно проверить всего одно условие: находится ли флаг в состоянии
# True. Все остальные проверки (которые должны определить, произошло ли собы-
# тие, переводящее флаг в состояние False) удобно организуются в остальном коде.
# Добавим флаг в программу parrot.py из предыдущего раздела. Этот флаг, который
# мы назовем active (хотя переменная может называться как угодно), управляет тем,
# должно ли продолжаться выполнение программы:

# prompt = "\nСкажи мне что-нибудь, и я тебе отвечу: "
# prompt += "\nВведи 'quit' чтоб завершить программу. "
#
# active = True   # 1
# while active:   # 2
#     message = input(prompt)
#
#     if message == 'quit':    # 3
#         active = False
#     else:                    # 4
#         print(message)


# В точке  переменной active присваивается True, чтобы программа начинала
# работу в активном состоянии. Это присваивание упрощает команду while, потому
# что в самой команде while никакие сравнения не выполняются; вся логика реали-
# зуется в других частях программы. Пока переменная active остается равной True,
# цикл выполняется.
# В команде if внутри цикла while значение message проверяется после того, как
# пользователь введет данные. Если пользователь ввел строку 'quit' , флаг active
# переходит в состояние False, а цикл while останавливается. Если пользователь ввел
# любой текст, кроме 'quit' , то введенные им данные выводятся как сообщение.
# Результаты работы этой программы ничем не отличаются от предыдущего приме-
# ра, в котором условная проверка выполняется прямо в команде while. Но теперь
# в программе имеется флаг, указывающий, находится ли она в активном состоянии,
# и вы сможете легко добавить новые проверки (в форме команд elif) для событий,
# с которыми переменная active может перейти в состояние False. Это может быть
# удобно в сложных программах — например, в компьютерных играх с многочислен-
# ными событиями, каждое из которых может привести к завершению программы.
# Когда по любому из этих событий флаг active переходит в состояние False, основ-
# ной игровой цикл прервется, выводится сообщение о завершении игры, и у игрока
# появляется возможность сыграть еще раз.

# -----------------------------------------------------------------------------------------------

# Команда break и выход из цикла

# prompt = "\nПожалуйста, введите название города, который бы вы хотели посетить: "
# prompt += "\n(Когда закончите, введите 'quit'.)"
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print("Я бы хотел поехать в " + city.title() + '!')


# Команда break может использоваться в любых циклах Python. Например, ее можно вклю-
# чить в цикл for для перебора элементов словаря.

# ------------------------------------------------------------------------------------------------------------------

# Команда continue и продолжение цикла

# Вместо того чтобы полностью прерывать выполнение цикла без выполнения остав-
# шейся части кода, вы можете воспользоваться командой continue для возвращения
# к началу цикла и проверке условия. Например, возьмем цикл, который считает от 1
# до 10, но выводит только нечетные числа в этом диапазоне:

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2:
#         continue
#     print(current_number)


# -------------------------------------------------------------------------------------------------------------------

# Предотвращение зацикливания

# У каждого цикла while должна быть предусмотрена возможность завершения, что-
# бы цикл не выполнялся бесконечно. Например, следующий цикл считает от 1 до 5:

# x = 1
# while x <= 5:
#     print(x)
#     x += 1


# Но если случайно пропустить строку x += 1 (см. далее), то цикл будет выполняться
# бесконечно:

# Бесконечный цикл!

# x = 1
# while x <= 5:
#     print(x)

# Теперь переменной x присваивается начальное значение 1, но это значение никог-
# да не изменяется в программе. В результате проверка условия x <= 5 всегда дает
# результат True, и цикл while выводит бесконечную серию единиц:

# ------------------------------------------------------------------------------------------------------------------

# УПРАЖНЕНИЯ:
# 7-4. Дополнения для пиццы: напишите цикл, который предлагает пользователю вводить
# дополнения для пиццы до тех пор, пока не будет введено значение 'quit’. При вводе каждо-
# го дополнения выведите сообщение о том, что это дополнение включено в заказ.

# pizza = "Введите дополнения для пицы, какие ингридиенты вы хотели бы добавить:\n "
# pizza += "(Когда закончите, введите 'quit')"
#
# while True:
#     ingridiens = input(pizza)
#     if ingridiens == 'quit':
#         break
#     else:
#         print(ingridiens.title() + ":" + " этот ингридиент включён в заказ" + ".")


# --------------------------------------------------------------------------------------------------------------------

# 7-5. Билеты в кино: кинотеатр установил несколько вариантов цены на билеты в зависимо-
# сти от возраста посетителя. Для посетителей младше 3 лет билет бесплатный; в возрасте
# от 3 до 12 билет стоит $10; наконец, если возраст посетителя больше 12, билет стоит $15.
# Напишите цикл, который предлагает пользователю ввести возраст и выводит цену билета.

# ages = "\t\tВведите ваш возраст:\n "
# ages += "(Для выхода из программы, введите 'quit')"
#
#
# while True:
#
#     age = input(ages)
#
#     if str(age) == 'quit':
#         break
#     elif int(age) < 3:
#         print("\nДля " + str(age) + " лет. Стоимость прохода бесплатная \n")
#     elif int(age) <= 12:
#         print("\nДля " + str(age) + " лет. Стоимость прохода 10$ \n")
#     else:
#         print("\nДля " + str(age) + " лет. Стоимость прохода билет стоит $15")

# -------------------------------------------------------------------------------------------------------------------

# 7-6. Три выхода: напишите альтернативную версию упражнения 7-4 или упражнения 7-5,
# в которой каждый пункт следующего списка встречается хотя бы один раз.
# • Завершение цикла по проверке условия в команде while.
# • Управление продолжительностью выполнения цикла в зависимости от переменной
# active.
# • Выход из цикла по команде break, если пользователь вводит значение ‘quit’.

# уже сделал

# --------------------------------------------------------------------------------------------------------------------

# 7-7. Бесконечный цикл: напишите цикл, который никогда не завершается, и выполните его.
# (Чтобы выйти из цикла, нажмите Ctrl+C или закройте окно с выводом.)

# numbers = 1

# while numbers <= 10:
#     print(numbers)

# --------------------------------------------------------------------------------------------------------------------

# Использование цикла while со списками и словарями

# До настоящего момента мы работали только с одним фрагментом информации,
# полученной от пользователя. Мы получали ввод пользователя, а затем выводили
# ответ на него. При следующем проходе цикла while программа получала новое
# входное значение и реагировала на него. Но, чтобы работать с несколькими
# фрагментами информации, необходимо использовать в циклах while списки
# и словари.
# Цикл for хорошо подходит для перебора списков, но, скорее всего, список не дол-
# жен изменяться в цикле, потому что у Python возникнут проблемы с отслежива-
# нием элементов. Чтобы изменять список в процессе обработки, используйте цикл
# while. Использование циклов while со списками и словарями позволяет собирать,
# хранить и упорядочивать большие объемы данных для последующего анализа
# и обработки.
# Возьмем список недавно зарегистрированных, но еще не проверенных пользова-
# телей сайта. Как переместить пользователей после проверки в отдельный список
# проверенных пользователей? Одно из возможных решений: используем цикл while
# для извлечения пользователей из списка непроверенных, проверяем их и включаем
# в отдельный список проверенных пользователей. Код может выглядеть так:


# unconfirmed_users = ['alice', 'brian', 'candace']  #  Начнём с двух списков: пользователей для проверки
# confirmed_users = [] #  И пустого списка для хранения проверенных пользователей.

# while unconfirmed_users:   # Проверяем каждого пользователя, пока остаются непроверенные пользователи.
#     current_user = unconfirmed_users.pop() # Каждый пользователь, прошедший проверку, перемещаются в список проверенных.
#     print("Подтверждённый пользователь: " + current_user.title())
#     confirmed_users.append(current_user)
#
# Вывод всех проверенных пользователей
# print("\nПподтвержденны следующие пользователи:")
# for confirmed_user in  confirmed_users:
#     print(confirmed_user.title())

# --------------------------------------------------------------------------------------------------------------------

# Удаление всех вхождений конкретного значения из списка

# В главе 3 функция remove() использовалась для удаления конкретного значения
# из списка. Функция remove() работала, потому что интересующее нас значение
# встречалось в списке только один раз. Но что если вы захотите удалить все вхож-
# дения значения из списка?
# Допустим, имеется список pets, в котором значение 'cat' встречается многократно.
# Чтобы удалить все экземпляры этого значения, можно выполнять цикл while до
# тех пор, пока в списке не останется ни одного экземпляра 'cat':

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)

# ---------------------------------------------------------------------------------------------------------------------

# Заполнение словаря данными, введенными пользователем

# responses = {}
#
# polling_activate = True  # установить флаг продолжения опроса.
#
# while polling_activate:
#     name = input("\nКак твоё имя? ")  # Запрос имени и ответа пользователя.
#     response = input("На какую гору ты когда-нибудь захочешь подняться? ")
#     responses[name] = response  # Ответ сохраняется в словаре:
#     repeat = input("Вы бы хотели, чтобы другой человек ответил? (yes/no) ")
#     if repeat == 'no':  # Проверка продолжения опроса.
#         polling_activate = False
#     print("\n---Результаты опроса---")  # Опрос завершён, вывести результат.
#     for name, response in responses.items():
#         print(name + " хотел бы подняться " + response + ".")

# ---------------------------------------------------------------------------------------------------------------------

# УПРАЖНЕНИЯ
# 7-8. Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями раз-
# личных видов сэндвичей. Создайте пустой список с именем finished_sandwiches. В цикле
# переберите элементы первого списка и выведите сообщение для каждого элемента (напри-
# мер, «I made your tuna sandwich»). После этого каждый сэндвич из первого списка пере-
# мещается в список finished_sandwiches. После того как все элементы первого списка будут
# обработаны, выведите сообщение с перечислением всех изготовленных сэндвичей.

# sandwich_orders = ['колбасой', 'сыром', 'панини', 'крок-мадам']
# finished_sandwiches = []
#
# while sandwich_orders:
#     sandwiches = sandwich_orders.pop()
#     print('Я сделал твой бутерброд с ' + sandwiches.title())
#     finished_sandwiches.append(sandwiches.title())
#
# print('\n')
#
# for finished_sandwiche in finished_sandwiches:
#     print('Мы приготовили сэндвичи: ' + finished_sandwiche)

# -------------------------------------------------------------------------------------------------------------------

# 7-9. Без пастрами: используя список sandwich_orders из упражнения 7-8, проследите за
# тем, чтобы значение ‘pastrami’ встречалось в списке как минимум три раза. Добавьте в на-
# чало программы код для вывода сообщения о том, что пастрами больше нет, и напишите
# цикл while для удаления всех вхождений ‘pastrami’ из sandwich_orders. Убедитесь в том, что
# в finished_sandwiches значение ‘pastrami’ не встречается ни одного раза.

# sandwich_orders = ['колбасой', 'pastrami', 'сыром', 'pastrami', 'панини', 'крок-мадам', 'pastrami']
# finished_sandwiches = []
#
# print('Показываем что список полный: ' + '\n' + str(sandwich_orders) + '\n')
#
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print('Смотрим что мы удалили слово по условию:' + '\n' + str(sandwich_orders) + '\n')
#
# for sandwich in sandwich_orders:
#     finished_sandwiches.append(sandwich)
# print('Проверяем что переложили в другой список: ' + '\n' + str(finished_sandwiches))

# -------------------------------------------------------------------------------------------------------------------

# 7-10. Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они
# хотели провести отпуск. Включите блок кода для вывода результатов опроса.

# users = {}

# vacation = True

# while vacation:
#     name = input("Как ваше имя? ")
#     user = input(str(name).title() + " где бы вы хотели провести свой отпуск? ")
#     users[name] = user
#     repeat = input("Вы хотели задать вопрос кому то ещё? (yes/no) ")
#     if repeat == "no":
#         vacation = False
# print("\n\t---Результат Опроса---")

# for key, value in users.items():
#     print(str(key).title() + " хотел проверсти отпуск в " + str(value).title() + ".")






