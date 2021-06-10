import csv
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib import pyplot as pl

# Чтение дат и температурных максимумов из файла.
filename = 'D:\Python library\gitTutorial\CSV & JSON\data\death_valley_2018_full.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

    high = int(row[6])
    highs.append(high)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Фоматирование диаграммы.
plt.title("Ежедневная температура, 2018-01-06")
plt.xlabel('')

fig.autofmt_xdate()
plt.ylabel("Температура (F)")
plt.tick_params(axis='both', which='major')

plt.show()


