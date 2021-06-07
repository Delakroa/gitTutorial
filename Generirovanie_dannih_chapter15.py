# Генерирование данных
#
# Под визуализацией данных понимается исследование данных через их визуальное
# представление. Визуализация тесно связана с анализом данных (data mining), ис-
# пользующим программный код для изучения закономерностей и связей в наборе
# данных. Набором данных может быть как маленький список чисел, помещающийся
# в одной строке кода, так и массивом из многих гигабайт.
# Качественное представление данных не сводится к красивой картинке. Если для
# набора данных подобрано простое, визуально привлекательное представление,
# его смысл становится очевидным для зрителя. Люди замечают в наборе данных
# закономерности, о которых они и не подозревали.
# К счастью, для визуализации сложных данных не нужен суперкомпьютер. Бла-
# годаря эффективности Python вы сможете быстро исследовать наборы данных
# из миллионов отдельных элементов данных (точек данных) на обычном ноутбуке.
# Элементы данных даже не обязаны быть числовыми. Приемы, о которых вы узнали
# в первой части книги, позволят вам проанализировать даже нечисловые данные.
# Python используется для обработки данных в генетике, исследовании климата, по-
# литическом и экономическом анализе и множестве других областей. Специалисты
# по обработке данных написали на Python впечатляющий инструментарий визуа-
# лизации и анализа, и многие из этих разработок также доступны и для вас. Один
# из самых популярных инструментов такого рода — matplotlib, математическая
# библиотека построения диаграмм. С помощью matplotlib можно строить простые
# диаграммы, графики, диаграммы разброса данных и т. д. После этого будет создан
# более интересный набор данных, основанный на концепции случайного блужда-
# ния — визуализации, генерируемой на базе серии случайных решений.
# Также в этом проекте будет использоваться пакет Pygal, ориентированный
# на создание
# визуализаций, хорошо работающих с цифровыми устройствами.
# С помощью Pygal можно выделять и изменять размеры элементов в ходе взаимо-
# действия пользователя с визуализацией; кроме того, размер визуализации легко
# изменяется под крошечные «умные часы» или гигантский монитор. Мы используем
# Pygal для исследования закономерностей различных бросков кубиков.

# ---------------------------------------------------------------------------------------------------------------------

# Установка matplotlib
#
# Сначала необходимо установить библиотеку matplotlib, которая будет исполь-
# зоваться в исходном наборе визуализаций. Если вы еще не использовали про310
# Глава 15 • Генерирование данных
# грамму pip, обращайтесь к разделу «Установка пакетов Python с использованием
# pip»
#
# В Linux
# Если вы используете версию Python, входящую в поставку системы, вы сможете
# использовать менеджер пакетов своей системы для установки matplotlib всего
# одной командой:
#
# $ sudo apt-get install python3-matplotlib
#
# Если вы используете Python 2.7, команда выглядит так:
# $ sudo apt-get install python-matplotlib
#
# Если у вас установлена более новая версия Python, вам придется установить еще
# несколько библиотек, от которых зависит matplotlib:
#
# $ sudo apt-get install python3.5-dev python3.5-tk tk-dev
# $ sudo apt-get install libfreetype6-dev g++
#
# Затем программа pip используется для установки matplotlib:
# $ pip install --user matplotlib
#
# В OS X
#
# Компания Apple включает matplotlib в свою стандартную установку Python. Что-
# бы проверить, установлена ли библиотека в вашей системе, откройте терминальный
# сеанс и попробуйте импортировать matplotlib. Если библиотека matplotlib еще
# не установлена в системе и вы использовали Homebrew для установки Python,
# установите ее следующей командой:
# $ pip install --user matplotlib
#
# ПРИМЕЧАНИЕ
# Возможно, при установке пакетов вам придется использовать команду pip3 вместо pip. Если же эта
# команда не работает, попробуйте исключить флаг --user.
#
# В Windows
# В системе Windows сначала необходимо установить Visual Studio. Откройте стра-
# ницу https://dev.windows.com/, щелкните на ссылке Скачать средства (Downloads)
# и найдите Visual Studio Community — бесплатный набор средств разработчика для
# Windows. Загрузите и запустите программу установки.
# Затем вам понадобится программа установки для matplotlib. Обратитесь по
# адресу https://pypi.python.org/pypi/matplotlib/ и найдите файл с расширени-
# ем .whl, соответствующий используемой версии Python. Например, если вы
# используете
# 32-разрядную версию Python 3.5, загрузите файл matplotlib-1.4.3-
# cp35-none-win32.whl.
#
# ПРИМЕЧАНИЕ
# Если вы не нашли файл, соответствующий используемой версии Python, просмотрите возможные
# варианты по адресу http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib. На этом сайте новые па-
# кеты появляются немного ранее, чем на официальном сайте matplotlib.
# Скопируйте файл .whl в каталог проекта, откройте окно командной строки
# и перейдите
# в каталог проекта. Используйте pip для установки matplotlib:
# > cd python_work
# python_work> python -m pip install --user matplotlib-1.4.3-cp35-none-win32.whl

# Тестирование matplotlib
#
# После того как необходимые пакеты будут установлены, протестируйте свою уста-
# новку. Для этого откройте сеанс командной строки командой python или python3
# и импортируйте matplotlib:
#
# $ python3
# >>> import matplotlib
# >>>
#
# Если на экране не появились сообщения об ошибках, значит, библиотека matplotlib
# установлена в вашей системе и вы можете переходить к следующему разделу.
#
# ПРИМЕЧАНИЕ
# Если у вас возникнут проблемы с установкой, поищите информацию в приложении В. Если ничего
# не помогает, обратитесь за помощью. Скорее всего, опытный программист Python быстро найдет
# причины возникших проблем с минимумом информации от вас.

# Галерея matplotlib
# Чтобы получить представления о визуализациях, которые можно строить
# в matplotlib, посетите галерею на сайте http://matplotlib.org/. Щелкая на визуали-
# зации в галерее, вы сможете просмотреть код, использованный для ее построения.

# ---------------------------------------------------------------------------------------------------------------------

# Построение простого графика

# Начнем с построения простого линейного графика с использованием matplotlib,
# а затем настроим его для более содержательной визуализации данных. В качестве
# данных для графика будет использоваться последовательность квадратов 1, 4, 9,
# 16 и 25.
# Передайте matplotlib числа так, как показано ниже, а matplotlib сделает все
# остальное:

# mpl_squares.py
#
# import matplotlib.pyplot as plt
# squares = [1, 4, 9, 16, 25]
# plt.plot(squares)
# plt.show()

# Сначала импортируйте модуль pyplot с псевдонимом plt, чтобы вам не приходи-
# лось многократно вводить имя pyplot. (Это сокращение часто встречается в приме-
# рах на сайте, поэтому мы поступим так же.) Модуль pyplot содержит ряд функций
# для построения диаграмм и графиков.
# Мы создаем список для хранения квадратов и передаем его функции plot(), ко-
# торая пытается построить осмысленное графическое представление для заданных
# чисел. Вызов plt.show() открывает окно просмотра matplotlib и выводит график
# (рис. 15.1). В окне просмотра можно изменять масштаб и перемещаться по по-
# строенному графику, а кнопка с диском позволяет сохранить любое изображение
# по вашему выбору.

# ---------------------------------------------------------------------------------------------------------------------

# Изменение типа надписей и толщины графика
#
# Хотя из графика на рис. 15.1 видно, что числовая последовательность возрастает,
# текст надписей слишком мелкий, а линия слишком тонкая. К счастью, matplotlib
# позволяет настроить практически каждый аспект визуализации.
# Мы используем эти возможности настройки для того, чтобы сделать график более
# выразительным:

# mpl_squares.py
#
# import matplotlib.pyplot as plt
#
# squares = [1, 4, 9, 16, 25]
#  plt.plot(squares, linewidth=5)
# # Назначение заголовка диаграммы и меток осей.
#  plt.title("Square Numbers", fontsize=24)
#  plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Назначение размера шрифта делений на осях.
#  plt.tick_params(axis='both', labelsize=14)
# plt.show()

# Параметр linewidth  управляет толщиной линии, которая строится вызо-
# вом plot(). Функция title()  назначает заголовок диаграммы. Параметры
# fontsize, неоднократно встречающиеся в коде, управляют размером текста
# диаграммы.
# Функции xlabel() и ylabel() позволяют назначить метки (заголовки) каж-
# дой из осей , а функция tick_params() определяет оформление делений на
# осях . Аргументы, использованные в данном примере, относятся к делениям
# на обоих
# осях (axes='both') и устанавливают для меток делений размер шрифта
# 14 (labelsize=14).
# Как видно из рис. 15.2, график выглядит гораздо лучше. Текст надписей стал круп-
# нее, а линия графика — толще.

# --------------------------------------------------------------------------------------------------------------------

# Корректировка графика
#
# Теперь, когда текст на графике стал нормально читаться, мы видим, что данные
# помечены неправильно. Обратите внимание: для точки 4,0 в конце графика указан
# квадрат 25! Давайте исправим эту ошибку.
# Если plot() передает числовую последовательность, функция считает, что первый
# элемент данных соответствует координате x со значением 0, но в нашем примере
# первая точка соответствует значению 1. Чтобы переопределить значение по умол-
# чанию, передайте plot() как входные значения, так и квадраты:

# Теперь, когда текст на графике стал нормально читаться, мы видим, что данные
# помечены неправильно. Обратите внимание: для точки 4,0 в конце графика указан
# квадрат 25! Давайте исправим эту ошибку.
# Если plot() передает числовую последовательность, функция считает, что первый
# элемент данных соответствует координате x со значением 0, но в нашем примере
# первая точка соответствует значению 1. Чтобы переопределить значение по умол-
# чанию, передайте plot() как входные значения, так и квадраты:

# mpl_squares.py
#
# import matplotlib.pyplot as plt
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)
# # Назначение заголовка диаграммы и меток осей.
# ...

# Теперь plot() правильно строит график, потому что мы предоставили оба набора
# значений, и функции не нужно предполагать, как был сгенерирован выходной на-
# бор чисел. На рис. 15.3 изображен правильный график.

# При вызове plot() можно передавать многочисленные аргументы, а также ис-
# пользовать различные функции для настройки графиков. Знакомство с этими
# функциями продолжится позднее, когда мы начнем работать с более интересными
# наборами данных в этой главе.

# ---------------------------------------------------------------------------------------------------------------------

# Нанесение и оформление отдельных точек функцией scatter()

# Иногда бывает полезно нанести на график отдельные точки, основанные на некото-
# рых характеристиках, и определить их оформление. Например, на графике малые
# и большие значения могут отображаться разными цветами. Возможны и другие
# варианты: например, сначала нанести множество точек с одним типом оформления,
# а затем выделить отдельные точки набора, перерисовав их с другим оформлением.
# Для нанесения на диаграмму отдельной точки используется функция scatter().
# Передайте scatter() координаты (x, y) нужной точки, и функция нанесет эти
# значения на диаграмму:

# scatter_squares.py
#
# import matplotlib.pyplot as plt
# plt.scatter(2, 4)
# plt.show()

# Применим оформление, чтобы результат выглядел более интересно. Мы добавим
# название, метки осей, а также увеличим шрифт, чтобы текст нормально читался:

# import matplotlib.pyplot as plt
#
#  plt.scatter(2, 4, s=200)
#
# # Назначение заголовка диаграммы и меток осей.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # Назначение размера шрифта делений на осях.
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()

# В точке  вызывается функция; аргумент s задает размер точек, используемых
# для рисования диаграммы. Если запустить программу scatter_squares.py в текущем
# состоянии, вы увидите одну точку в середине диаграммы

# --------------------------------------------------------------------------------------------------------------------

# Вывод серии точек функцией scatter()

# Чтобы вывести на диаграмме серию точек, передайте scatter() списки значений
# координат x и y:

# scatter_squares.py
#
# import matplotlib.pyplot as plt
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)
# # Назначение заголовка диаграммы и меток осей.
# ...

# Список x_values содержит числа, возводимые в квадрат, а в y_values содержатся
# квадраты. При передаче этих списков scatter() библиотека matplotlib читает
# по одному значению из каждого списка и наносит их на диаграмму как точку.
# Таким
# образом, на диаграмму будут нанесены точки (1, 1), (2, 4), (3, 9), (4, 16)
# и (5, 25);

# --------------------------------------------------------------------------------------------------------------------

# Автоматическое вычисление данных

# Строить списки вручную неэффективно, особенно при большом объеме данных.
# Вместо того чтобы передавать данные в виде списка, мы воспользуемся циклом
# Python, который выполнит вычисления за нас. Вот как выглядит такой цикл для
# 1000 точек:

# scatter_squares.py
#
# import matplotlib.pyplot as plt
#  x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
#  plt.scatter(x_values, y_values, s=40)
# Назначение заголовка диаграммы и меток осей.
# ...
# # Назначение диапазона для каждой оси.
# w plt.axis([0, 1100, 0, 1100000])
# plt.show()

# Все начинается со списка значений координаты x с числами от 1 до 1000 . Затем
# генератор списка строит значения y, перебирая значения x (for x in x_values), воз-
# водя каждое число в квадрат (x**2) и сохраняя результаты в y_values. Затем оба
# списка (входной и выходной) передаются scatter() .
# Набор данных достаточно велик, поэтому мы выбираем меньший размер шрифта,
# а функция axis() используется для задания диапазона каждой оси . Функция
# axis() получает четыре значения: минимум и максимум по осям x и y. В данном
# случае по оси x откладывается диапазон от 0 до 1100, а по оси y — диапазон от 0
# до 1 100 000. На рис. 15.6 показан результат.

# ---------------------------------------------------------------------------------------------------------------------

# Удаление контуров точек

# Библиотека matplotlib позволяет раскрашивать точки на точечной диаграмме
# в разные цвета. Оформление по умолчанию — синие точки с черным контуром —
# хорошо подходит для диаграмм с несколькими точками. Однако при большом
# количестве точек черные контуры начинают сливаться. Чтобы удалить контуры
# вокруг точек, передайте аргумент edgecolor='none' при вызове scatter():
# plt.scatter(x_values, y_values, edgecolor='none', s=40)
# Запустите scatter_squares.py с этим вызовом, и вы увидите, что на диаграмме выво-
# дятся только заполненные синие точки.

# --------------------------------------------------------------------------------------------------------------------

# Цветовые карты
#
# Цветовая карта (colormap) представляет собой серию цветов градиента, опре-
# деляющую плавный переход от начального цвета к конечному. Цветовые карты
# используются в визуализациях для выделения закономерностей в данных. Напри-
# мер, малые значения можно обозначить светлыми цветами, а большие — темными.
# Модуль pyplot включает набор встроенных цветовых карт. Чтобы воспользоваться
# одной из готовых карт, нужно указать, как модуль pyplot должен присваивать цвет
# каждой точке набора данных. В следующем примере цвет каждой точки присваи-
# вается на основании значения y:

# scatter_squares.py
#
# x_values = list(range(1001))
# y_values = [x**2 for x in x_values]
#
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
# edgecolor='none', s=40)
#
# # Назначение заголовка диаграммы и меток осей.
# ...

# Мы передаем в c список y-values, а затем указываем pyplot, какая цветовая
# карта должна использоваться, при помощи аргумента cmap. Следующий код
# окрашивает точки с меньшими значениями y в светло-синий цвет, а точки
# с бульшими значениями y — в темно-синий цвет.

# ПРИМЕЧАНИЕ
# Все цветовые карты, доступные в pyplot, можно просмотреть на сайте http://matplotlib.org/; от-
# кройте раздел Examples, прокрутите содержимое до пункта Color Examples и щелкните на ссылке
# colormaps_reference.

# --------------------------------------------------------------------------------------------------------------------

