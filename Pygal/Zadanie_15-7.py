import pygal

from die import Die

# Создайте два кубика D6.
die_1 = Die()
die_2 = Die()

# Сделайте несколько бросков и сохраните результаты в списке.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Анализируйте результаты.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Визуализируйте результаты.
hist = pygal.Bar()

hist.title = "Результаты броска двух кубиков D6 1000 раз."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Результаты"
hist.y_title = "Частота результатов"

hist.add('D6 + D6', frequencies)
hist.render_to_file('zadanie.svg')
