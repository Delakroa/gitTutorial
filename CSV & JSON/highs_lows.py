import csv

# Чтение максимальных температур из файла.
filename = 'D:\Python library\gitTutorial\CSV & JSON\data\death_valley_2018_full.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[6])
        highs.append(high)

print(highs)
