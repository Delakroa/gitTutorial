import csv

import matplotlib.pyplot as plt
from matplotlib import pyplot as pl

# Чтение максимальных температур из файла.
filename = 'D:\Python library\gitTutorial\CSV & JSON\data\death_valley_2018_full.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[6])
        highs.append(high)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# Фоматирование диаграммы.
plt.title("Ежедневная температура, 06-01-2018")
plt.xlabel('')
plt.ylabel("Температура (F)")
plt.tick_params(axis='both', which='major')

plt.show()


