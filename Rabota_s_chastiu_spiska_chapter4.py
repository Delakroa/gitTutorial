# ПЕРЕБОР СОДЕРЖИМОГО СРЕЗА:

# players = ['Вован', 'Диман', 'Олег', 'Алекс', 'Андрю']
# print("Вот первые три человека в моей бригаде:")
# for player in players[:3]:
#     print(player.title())

# -----------------------------------------------------------------------------------------------------------------
# КОПИРОВАНИЕ СПИСКА:

# my_zapchasti = ['болт', 'винт', 'гайка']
# zapchasti_druzei = my_zapchasti[:]
#
# print("Часто использумые запчасти у меня")
# print(my_zapchasti)
#
# print("\nЧасто используемые запчасти у друзей")
# print(zapchasti_druzei)

# Чтобы доказать, что речь в действительности идет о двух разных списках, добавим
# новое инструменты в каждый список:

# my_zapchasti = ['болт', 'винт', 'гайка']
# zapchasti_druzei = my_zapchasti[:]
#
# my_zapchasti.append('двигатель')
# zapchasti_druzei.append('шайба')
#
# print("Часто использумые запчасти у меня")
# print(my_zapchasti)
#
# print("\nЧасто используемые запчасти у друзей")
# print(zapchasti_druzei)


# 4-10. Срезы: добавьте в конец одной из программ, написанных в этой главе, фрагмент,
# который делает следующее.
# • Выводит сообщение «The first three items in the list are:», а затем использует срез для
# вывода первых трех элементов из списка.
# • Выводит сообщение «Three items from the middle of the list are:», а затем использует
# срез для вывода первых трех элементов из середины списка.
# • Выводит сообщение «The last three items in the list are:», а затем использует срез для
# вывода последних трех элементов из списка.
# Упражнение 4-10:
# my_foods = ['pizza', 'falafel', 'cofee', 'tea', 'carrot cake', 'cannoli', 'ice cream']
# print('Первые три пункта в списке:')
# for food in my_foods[0:3]:
#     print(food)
# print('Три пункта из середины списка:')
# for foods in my_foods[2:5]:
#     print(foods)
# print('Последние три пункта в списке:')
# for last_foods in my_foods[4:7]:
#     print(last_foods)

# Упражнение 4-11:
# 4-11. Моя пицца, твоя пицца: начните с программы из упражнения 4-1. Создайте копию
# списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее.
# • Добавьте новую пиццу в исходный список.
# • Добавьте другую пиццу в список friend_pizzas.
# • Докажите, что в программе существуют два разных списка. Выведите сообщение «My
# favorite pizzas are:», а затем первый список в цикле for. Выведите сообщение «My
# friend’s favorite pizzas are:», а затем второй список в цикле for. Убедитесь в том, что
# каждая новая пицца находится в соответствующем списке.


# friend_pizzas = ['салями', 'анчёусами', 'деревенская', 'народная', 'маргарита', 'сицилийская', 'капричоза']
# for friend in friend_pizzas[:]:
#     print(friend.title())

# ------------------------------------------------------------------------------------------------------------

# friend_pizzas = ['салями', 'анчёусами', 'деревенская', 'народная', 'маргарита', 'сицилийская', 'капричоза']
# friend = friend_pizzas[:]

# friend.append('диабло')
# friend_pizzas.append('гаспачо')
#
# print('«My favorite pizzas are:')
# print(friend)
#
# print('My friend’s favorite pizzas are:')
# print(friend_pizzas)

# ----------------------------------------------------------------------------------------------------

# friend_pizzas = ['салями', 'анчёусами', 'деревенская', 'народная', 'маргарита', 'сицилийская', 'капричоза']
#
# print('My favorite pizzas are:')
# friend_pizzas.append('диабло')
# print(friend_pizzas)
#
#
# print('My friend’s favorite pizzas are:')
# friend_pizzas.append('гаспачо')
# print(friend_pizzas)

# 4-12. Больше циклов: во всех версиях foods.py из этого раздела мы избегали использования
# цикла for при выводе для экономии места. Выберите версию foods.py и напишите два цикла
# for для вывода каждого списка.

friend_pizzas = ['салями', 'анчёусами', 'деревенская', 'народная', 'маргарита', 'сицилийская', 'капричоза']
# friend_pizza = friend_pizzas[:]
friend_pizzas.append('diablo')
friend_pizzas.append('gaspacho')
for friend_pizza in friend_pizzas:
    print('My favorite pizzas are ' + friend_pizza + '.')

