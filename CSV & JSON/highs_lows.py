import csv
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib import pyplot as pl

# Чтение дат и температурных максимумов из файла.
filename = 'data\death_valley_2018_full.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Получите даты и высокие температуры из этого файла.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%d-%m-%Y")
        dates.append(current_date)

        high = int(row[6])
        highs.append(high)

        low = int(row[7])
        lows.append(low)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs,  c='red')
plt.plot(dates, lows, c='blue')

# Фоматирование диаграммы.
plt.title("Ежедневные высокие и низкие температуры, 2018", fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Температура (F)", fontsize=16)
plt.tick_params(axis='both', which='major')

plt.show()


