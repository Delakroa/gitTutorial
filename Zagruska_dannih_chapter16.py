# Загрузка данных
#
# В этой главе мы загрузим наборы данных из сетевого источника и создадим рабо-
# тоспособные визуализации этих данных. В Интернете можно найти невероятно
# разнообразную информацию, бульшая часть которой еще не подвергалась осно-
# вательному анализу. Умение анализировать данные позволит вам выявить связи
# и закономерности, не найденные никем другим.
# В этой главе рассматривается работа с данными в двух популярных форматах,
# CSV и JSON. Модуль Python csv будет применен для обработки погодных данных
# в формате CSV (с разделением запятыми) и анализа динамики высоких и низких
# температур в двух разных местах. Затем библиотека matplotlib будет использована
# для построения на базе загруженных данных диаграммы изменения температур.
# Позднее в этой главе модуль json будет использован для обращения к данным
# численности населения, хранимым в формате JSON, а при помощи модуля Pygal
# будет построена карта распределения населения по странам.
# К концу этой главы вы будете готовы к работе с разными типами и форматами
# наборов данных и начнете лучше понимать принципы построения сложных визу-
# ализаций. Возможность загрузки и визуализации сетевых данных разных типов
# и форматов крайне важна для работы с разнообразными массивами данных в ре-
# альном мире.

# -------------------------------------------------------------------------------------------------------------------

# Формат CSV

# Один из простейших вариантов хранения — запись данных в текстовый файл как
# серий значений, разделенных запятыми; такой формат хранения получил название
# CSV (от Comma Separated Values, то есть «значения, разделенные запятыми»). На-
# пример, одна строка погодных данных в формате CSV может выглядеть так:
# 2014-1-5,61,44,26,18,7,-1,56,30,9,30.34,30.27,30.15,,,,10,4,,0.00,0,,195
# Это погодные данные за 5 января 2014 г. в Ситке (Аляска). В данных указаны мак-
# симальная и минимальная температуры, а также ряд других показателей за этот
# день. У человека могут возникнуть проблемы с чтением данных CSV, но этот фор-
# мат хорошо подходит для программной обработки и извлечения значений, а это
# ускоряет процесс анализа.
# Начнем с небольшого набора погодных данных в формате CSV, запи-
# санного в Ситке; файл с данными можно загрузить среди ресурсов книги
# по адресу https://www.nostarch.com/pythoncrashcourse/. Скопируйте файл
# sitka_weather_07-2014.csv в каталог, в котором сохраняются программы этой главы.
# (После загрузки ресурсов книги в вашем распоряжении появятся все необходимые
# файлы для этого проекта.)

# -------------------------------------------------------------------------------------------------------------------

