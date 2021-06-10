import csv

filename = 'D:\Python library\gitTutorial\CSV & JSON\data\death_valley_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


for index, column_header in enumerate(header_row):
    print(index, column_header)
