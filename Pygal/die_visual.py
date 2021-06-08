import pygal

from die import Die

# Создание кубика D6.
die = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результов.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = 'Результаты броска одного кубика D6 1000 раз.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Результат'
hist.y_title = 'Частота результатов'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')


print(frequencies)


