import pygal

from die import Die

# Создание кубика.
die = Die()

# Сделайте несколько бросков и сохраните результаты в списке.
results = [die.roll() for roll_num in range(1000)]

# Анализ результаты
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Визуализация результата
hist = pygal.Bar()

hist.title = 'Результаты броска одного D6 1000 раз'
hist.x_labels = [str(x) for x in range(1, die.num_sides+1)]
hist.x_title = "Результаты"
hist.y_title = "Частота результатов"

hist.add('D6', frequencies)
hist.render_to_file('zadanie.svg')
