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

# print('«My favorite pizzas are:')
# friend_pizzas.append('диабло')
# print(friend_pizzas)
#
#
# print('My friend’s favorite pizzas are:')
# friend_pizzas.append('гаспачо')
# print(friend_pizzas)
