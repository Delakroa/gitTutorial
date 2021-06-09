import csv

filename = 'https://www.gismeteo.ru/weather-tver-4327/'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
