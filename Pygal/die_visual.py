import pygal

from die import Die

# Создание кубика D6.
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = 'Результаты броска двух кубиков D6 1000 раз.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Результаты'
hist.y_title = 'Частота результатов'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')


print(frequencies)


