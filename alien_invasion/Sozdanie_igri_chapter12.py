# 12 Стреляющий корабль
#
# Давайте создадим собственную игру! Мы воспользуемся Pygame — подборкой ин-
# тересных, мощных модулей Python для управления графикой, анимацией и даже
# звуком, упрощающей построение сложных игр. Pygame берет на себя такие задачи,
# как перерисовка изображений на экране, что позволяет вам пропустить бульшую
# часть рутинного, сложного программирования и сосредоточиться на высокоуров-
# невой логике игровой динамики.
# В этой главе мы настроим Pygame и создадим корабль, который движется вле-
# во и вправо и стреляет по приказу пользователя. В следующих двух главах вы
# создадите
# флот инопланетного вторжения, а затем займетесь внесением усовер-
# шенствований — например, ограничением количества попыток и добавлением
# таблицы рекордов.
# Эта глава также научит вас управлять большими проектами, состоящими из многих
# файлов. Мы часто будем проводить рефакторинг и изменять структуру содержи-
# мого файлов, чтобы проект был четко организован, а код оставался эффективным.
# Программирование игр — идеальный способ совместить изучение языка с раз-
# влечением. Написание простой игры поможет вам понять, как пишутся профес-
# сиональные игры. В процессе работы над этой главой вводите и запускайте код,
# чтобы понять, как каждый блок кода участвует в общем игровом процессе. Экс-
# периментируйте с разными значениями и настройками, чтобы лучше понять, как
# следует организовать взаимодействие с пользователем в ваших собственных играх.
#
# ПРИМЕЧАНИЕ
# Игра Alien Invasion состоит из множества файлов; создайте в своей системе новый каталог с име-
# нем alien_invasion. Чтобы команды import работали правильно, все файлы проекта должны нахо-
# диться в этой папке.
#
# ланирование проекта
# Построение крупного проекта должно начинаться не с написания кода, а с плани-
# рования. План поможет вам направить усилия в нужном направлении и повысит
# вероятность успешного завершения проекта.
# Итак, напишем общее описание игрового процесса. Хотя это описание не затра-
# гивает все аспекты игры, оно дает достаточно четкое представление о том, с чего
# начинать работу:
#
# Каждый игрок управляет кораблем, который находится в середине нижнего края экрана.
# Игрок перемещает корабль вправо и влево клавишами управления или курсором; клавиша
# «пробел» используется для стрельбы. В начале игры флот пришельцев находится в верхней
# части экрана и постепенно опускается вниз, также смещаясь в сторону. Игрок выстрелами
# уничтожает пришельцев. Если ему удается сбить всех пришельцев, появляется новый флот,
# который движется быстрее предыдущего. Если пришелец сталкивается с кораблем игрока или
# доходит до нижнего края экрана, игрок теряет корабль. Если игрок теряет все три корабля,
# игра заканчивается.
#
# В первой фазе разработки мы создадим корабль, который может двигаться вправо
# и влево. Корабль должен стрелять из пушки, когда игрок нажимает клавишу «про-
# бел». Когда это поведение будет реализовано, мы сможем заняться пришельцами
# и доработкой игрового процесса.

# ---------------------------------------------------------------------------------------------------------------------

# Установка Pygame
# Прежде чем браться за программирование, установите пакет Pygame. Ниже описан
# процесс установки в Linux, OS X и Microsoft Windows.
# Если вы используете Python 3 в системе Linux или если вы работаете в OS X,
# для установки Pygame используется pip — программа, управляющая загрузкой
# и установкой пакетов Python. Процедура установки пакетов с использованием pip
# описана ниже.
# Если вы используете Python 2.7 в системе Linux или если вы работаете в Windows,
# для установки Pygame программа pip вам не понадобится. Вместо этого перейдите
# к разделу «Установка Pygame в Linux» (с. 229) или «Установка Pygame в Windows»
#
# ПРИМЕЧАНИЕ
# Далее приводятся инструкции по установке pip во всех системах, потому что эта программа пона-
# добится вам для визуализации данных и веб-приложений. Инструкции также доступны по адресу
# https://www.nostarch.com/pythoncrashcourse/. Если у вас возникнут проблемы с инструкциями, при-
# веденными ниже, попробуйте загрузить инструкции с сайта — возможно, они сработают.
#
# Установка пакетов Python с использованием pip
# В последних версиях Python pip устанавливается автоматически, поэтому сначала
# проверьте, присутствует ли эта программа в вашей системе. В Python 3 программа
# pip иногда называется pip3.
#
# Проверка pip в Linux и OS X
# Откройте терминальное окно и введите следующую команду:
# $ pip --version
#  pip 7.0.3 from /usr/local/lib/python3.5/dist-packages (python 3.5)
# Если в вашей системе установлена только одна версия Python и вы получили при-
# мерно такой результат, переходите к разделу «Установка Pygame в Linux» (с. 229)
# или «Установка Pygame в OS X» (с. 230). Если вы получите сообщение об ошибке,
# попробуйте ввести имя pip3 вместо pip. Если ни одна версия не установлена в вашей
# системе, обратитесь к разделу «Установка pip» (c. 228).
# Если в вашей системе установлено несколько версий Python, проверьте, что про-
# грамма pip связана с используемой версией — например, Python 3.5 . Если про-
# грамма pip связана с правильной версией, переходите к разделу «Установка Pygame
# в Linux» (с. 229) или «Установка Pygame в OS X» (с. 230). Если версия неправиль-
# ная, попробуйте ввести имя pip3 вместо pip. Если ни одна команда не работает для
# вашей версии Python, обратитесь к разделу «Установка pip» (c. 228).
# Проверка pip в Windows
# Откройте окно командной строки и введите следующую команду:
# $ python -m pip --version
#  pip 7.0.3 from C:\Python35\lib\site-packages (python 3.5)
# Если в вашей системе установлена только одна версия Python, и вы получили
# примерно такой результат, переходите к разделу «Установка Pygame в Windows»
# (с. 231). Если вы получите сообщение об ошибке, попробуйте ввести имя pip3 вме-
# сто pip. Если ни одна версия не установлена в вашей системе, обратитесь к разделу
# «Установка pip» (с. 228).
# Если в вашей системе установлено несколько версий Python, проверьте, что про-
# грамма pip связана с используемой версией, например Python 3.5 . Если про-
# грамма pip связана с правильной версией, переходите к разделу «Установка Pygame
# в Windows» (с. 231). Если версия неправильная, попробуйте ввести имя pip3 вместо
# pip. Если ни одна команда не работает для вашей версии Python, обратитесь к сле-
# дующему разделу «Установка pip».
# Установка pip
# Чтобы установить pip, обратитесь по адресу https://bootstrap.pypa.io/get-pip.py. Со-
# храните файл, если вам будет предложено. Если код get-pip.py появится в браузере,
# скопируйте код в текстовый редактор и сохраните в файле с именем get-pip.py.
# После того как программа get-pip.py будет сохранена на вашем компьютере, ее не-
# обходимо будет запустить с административными привилегиями, потому что pip
# будет устанавливать новые пакеты в вашей системе.
#
# ПРИМЕЧАНИЕ
# Если вы не нашли программу get-pip.py, обратитесь по адресу https://pip.pypa.io/, щелкните
# на ссылке Installation на левой панели, а затем в разделе Install pip перейдите по ссылке для за-
# грузки get-pip.py.
# Установка Pygame 229
# Установка pip в Linux и OS X
# Чтобы запустить get-pip.py с административными привилегиями, введите следующую
# команду:
# $ sudo python get-pip.py
# ПРИМЕЧАНИЕ
# Если терминальный сеанс был запущен командой python3, используйте команду sudo python3 getpip.
# py.
# После выполнения программы введите команду pip --version (или pip3 --version),
# чтобы убедиться в том, что программа pip была установлена правильно.
# Установка pip в Windows
# Чтобы запустить get-pip.py, введите следующую команду:
# $ python get-pip.py
# Если для запуска Python в терминале использовалась другая команда, проследите
# за тем, чтобы программа get-pip.py запускалась этой же командой — например,
# python3 get-pip.py или C:\Python35\python get-pip.py.
# После выполнения программы введите команду python -m pip --version, чтобы
# убедиться в том, что программа pip была установлена правильно.
# Установка Pygame в Linux
# Если вы используете Python 2.7, установите Pygame при помощи менеджера паке-
# тов. Откройте терминальное окно и введите следующую команду, которая загрузит
# и установит Pygame в вашей системе:
# $ sudo apt-get install python-pygame
# Проверьте правильность установки в терминальном сеансе; для этого введите
# следующую команду:
# $ python
# >>> import pygame
# >>>
# Если никаких дополнительных сообщений нет, значит, импортирование Pygame
# прошло успешно, и вы можете переходить к разделу «Создание проекта игры»
# на с. 231.
# Если вы используете Python 3, процесс состоит из двух шагов: установки библио-
# тек, от которых зависит Pygame, и загрузки/установки Pygame.
# Чтобы установить библиотеки, необходимые Pygame, введите следующую команду
# (если в вашей системе используется другая команда, например python3.5, замените
# python3-dev на python3.5-dev).
# $ sudo apt-get install python3-dev mercurial
# $ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
# 230 Глава 12 • Стреляющий корабль
# Эти команды установят библиотеки, необходимые для успешного запуска игры
# Alien Invasion. Если вы хотите включить расширенную функциональность Pygame
# (например, возможность добавления звуков), добавьте следующие библиотеки:
# $ sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
# $ sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
# $ sudo apt-get install python-numpy
# Теперь установите Pygame следующей командой (используйте pip3, если эта ко-
# манда соответствует вашей системе):
# $ pip install --user hg+http://bitbucket.org/pygame/pygame
# После небольшой паузы программа сообщает, какие библиотеки были найдены.
# Нажмите Enter, даже если некоторые библиотеки отсутствуют. Вы увидите со-
# общение об успешной установке Pygame.
# Чтобы проверить правильность установки, откройте терминальный сеанс и попро-
# буйте импортировать Pygame:
# $ python3
# >>> import pygame
# >>>
# Если импортирование прошло нормально, переходите к разделу «Создание про-
# екта игры» на с. 231.
# Установка Pygame в OS X
# Для установки некоторых пакетов, от которых зависит Pygame, вам понадобится
# менеджер пакетов Homebrew. Если в вашей системе он еще не установлен, обра-
# щайтесь к приложению А за инструкциями.
# Чтобы установить библиотеки, от которых зависит Pygame, введите следующую
# команду:
# $ brew install hg sdl sdl_image sdl_ttf
# Команда устанавливает библиотеки, необходимые для Alien Invasion. В процессе
# установки каждой библиотеки на экране должна выводиться соответствующая
# информация.
# Если вы хотите включить расширенную функциональность (например, возмож-
# ность добавления звуков), добавьте еще две библиотеки:
# $ brew install sdl_mixer portmidi
# Установите Pygame следующей командой (используйте pip вместо pip3, если вы
# используете Python 2.7):
# $ pip3 install --user hg+http://bitbucket.org/pygame/pygame
# Чтобы проверить правильность установки, откройте терминальный сеанс и по-
# пробуйте импортировать Pygame (используйте python вместо python3, если вы
# используете Python 2.7):
# Создание проекта игры 231
# $ python3
# >>> import pygame
# >>>
# Если импортирование прошло нормально, переходите к разделу «Создание про-
# екта игры».
# Установка Pygame в Windows
# Проект Pygame размещен на сайте совместного использования кода Bitbucket.
# Чтобы установить Pygame для вашей версии Windows, найдите на странице https://
# bitbucket.org/pygame/pygame/downloads/ программу установки для Windows,
# соответствующую
# вашей версии Python. Если вы не нашли подходящую программу
# установки на сайте Bitbucket, попробуйте поискать по адресу http://www.lfd.uci.
# edu/~gohlke/pythonlibs/#pygame.
# Когда подходящий файл будет загружен, запустите программу установки, если это
# файл с расширением .exe.
# Если файл имеет суффикс .whl, скопируйте его в каталог проекта. Откройте окно
# командной строки, перейдите в папку, в которую был скопирован установочный
# пакет, и воспользуйтесь программой pip для запуска установки:

# > python -m pip install --user pygame-1.9.2a0-cp35-none-win32.whl

# ---------------------------------------------------------------------------------------------------------------------
#
# Создание проекта игры
# Построение игры начнется с создания пустого окна Pygame, в котором позднее
# будут отображаться игровые элементы — прежде всего корабль и пришельцы.
# Также игра должна реагировать на действия пользователя, назначать цвет фона
# и загружать изображение корабля.

# ---------------------------------------------------------------------------------------------------------------------

# Создание окна Pygame и обработка ввода

# import sys
#
# import pygame
#
#
# def run_game():
#     """Инициализирует игру и создаёт объект экрана."""
#     pygame.init()   # 1
#     screen = pygame.display.set_mode((1200, 800))   # 2
#     pygame.display.set_caption("Alien Invasion")
#
#     # Запуск основного цикла игры.
#
#     while True:   # 3
#         # Отслеживание событий клавиатуры и мыши.
#         for event in pygame.event.get():   # 4
#             if event.type == pygame.QUIT:   # 5
#                 sys.exit()
#
#         # Отображение последнего прорисованного экрана.
#         pygame.display.flip()    # 6
#
#
# run_game()

# Программа начинается с импортирования модуля sys и pygame. Модуль pygame
# содержит функциональность, необходимую для создания игры, а модуль sys
# завершает
# игру по команде игрока.
# Игра Alien Invasion начинается с определения функции run_game(). Строка pygame.
# init()  инициализирует настройки, необходимые Pygame для нормальной ра-
# боты. В точке  вызов pygame.display.set_mode() создает отображаемую область
# screen, на которой прорисовываются все графические элементы игры. Аргумент
# (1200, 800) представляет собой кортеж, определяющий размеры игрового окна.
# Передавая эти размеры pygame.display.set_mode(), мы создаем игровое окно с ши-
# риной 1200 пикселов и высотой 800 пикселов. (Вы можете изменить эти значения
# в соответствии с размерами своего монитора.)
# Объект screen называется поверхностью (surface). Поверхность в Pygame пред-
# ставляет часть экрана, на которой отображается игровой элемент. Каждый элемент
# в игре (например, пришелец или корабль игрока) представлен поверхностью.
# Поверхность, возвращаемая display.set_mode(), представляет все игровое окно.
# При активизации игрового цикла анимации эта поверхность автоматически пере-
# рисовывается при каждом проходе цикла.
# Процессом игры управляет цикл while , который содержит цикл событий и код,
# управляющий обновлениями экрана. Событием называется действие, выполняе-
# мое пользователем во время игры (например, нажатие клавиши или перемещение
# мыши). Чтобы наша программа реагировала на события, мы напишем цикл со-
# бытий для прослушивания событий и выполнения соответствующей операции
# в зависимости от типа произошедшего события. Этим циклом событий является
# цикл for в точке .
# Чтобы получить доступ к событиям, обнаруженным Pygame, мы используем метод
# pygame.event.get(). При любом событии клавиатуры или мыши отрабатывает
# цикл for. В этом цикле мы пишем серию команд if для обнаружения и обработки
# конкретных событий. Например, когда игрок щелкает на кнопке закрытия игрового
# окна, программа обнаруживает событие pygame.QUIT, и программа вызывает метод
# sys.exit() для выхода из игры .
# Вызов pygame.display.flip()  приказывает Pygame отобразить последний от-
# рисованный экран. В данном случае при каждом выполнении цикла while будет
# отображаться пустой экран со стиранием старого экрана, так что виден будет только
# новый экран. При перемещении игровых элементов вызов pygame.display.flip()
# будет постоянно обновлять экран, отображая игровые элементы в новых позици-
# ях и скрывая старые изображения; таким образом создается иллюзия плавного
# движения.
# Последняя строка в этой базовой структуре вызывает метод run_game(), который
# инициализирует игру и запускает основной цикл.
# Запустите этот код, и вы увидите пустое окно Pygame.

# ---------------------------------------------------------------------------------------------------------------------

# Назначение цвета фона
# Pygame по умолчанию создает черный экран, но это банально. Выберем другой
# цвет фона:

# alien_invasion.py
# ...
# def run_game():
# ...
# pygame.display.set_caption("Alien Invasion")
# # Назначение цвета фона.
#  bg_color = (230, 230, 230)
# # Запуск основного цикла игры.
# while True:
# # Отслеживание событий клавиатуры и мыши.
# ...
# # При каждом проходе цикла перерисовывается экран.
#  screen.fill(bg_color)
# # Отображение последнего прорисованного экрана.
# pygame.display.flip()
# run_game()

# Сначала программа создает цвет фона и сохраняет его в переменной bg_color .
# Цвет достаточно задать только один раз, поэтому его значение определяется до вхо-
# да в основной цикл while.
# Цвета в Pygame задаются в схеме RGB: тройками интенсивности красной, зеленой
# и синей составляющих цвета. Значение каждой составляющей лежит в диапазоне
# от 0 до 255. Цветовое значение (255, 0, 0) соответствует красному цвету, (0, 255,
# 0) — зеленому и (0, 0, 255) — синему. Разные сочетания составляющих RGB позво-
# ляют создать до 16 миллионов цветов. В цветовом значении (230, 230, 230) красная,
# синяя и зеленая составляющие смешиваются в равных долях, давая светло-серый
# цвет фона.
# В точке  экран заполняется цветом фона. Для этого вызывается метод screen.
# fill(), получающий всего один аргумент: цвет фона.

# --------------------------------------------------------------------------------------------------------------------

# Создание класса Settings

# Каждый раз, когда в нашу игру добавляется новая функциональность, также в нее
# обычно добавляются новые настройки (параметры конфигурации). Вместо того
# чтобы добавлять настройки в коде, мы напишем модуль с именем settings; этот
# модуль содержит класс с именем Settings для хранения всех настроек. Такое
# решение позволит передавать один объект вместо множества отдельных настро-
# ек. Кроме того, оно упрощает вызовы функций и упрощает изменение внешнего
# вида игры с ростом проекта. Чтобы внести изменения в игру, достаточно будет
# изменить некоторые значения в settings.py вместо того, чтобы искать разные на-
# стройки в файлах.
# Исходная версия класса Settings выглядит так:

# settings.py
# class Settings():
# """Класс для хранения всех настроек игры Alien Invasion."""
# def __init__(self):
# """Инициализирует настройки игры."""
# # Параметры экрана
# self.screen_width = 1200
# self.screen_height = 800
# self.bg_color = (230, 230, 230)
# Чтобы создать экземпляр Settings и использовать его для обращения к настройкам,
# внесите изменения в alien_invasion.py:
# alien_invasion.py
# ...
# import pygame
# from settings import Settings
# def run_game():
# # Инициализирует pygame, settings и объект экрана.
# pygame.init()
#  ai_settings = Settings()
#  screen = pygame.display.set_mode(
# (ai_settings.screen_width, ai_settings.screen_height))
# pygame.display.set_caption("Alien Invasion")
# # Запуск основного цикла игры.
# while True:
# ...
# # При каждом проходе цикла перерисовывается экран.
#  screen.fill(ai_settings.bg_color)
# # Отображение последнего прорисованного экрана.
# pygame.display.flip()
# run_game()
# Класс Settings импортируется в основной файл программы, после чего программа
# создает экземпляр Settings и сохраняет его в ai_settings после вызова pygame.
# init() . При создании экрана  используются атрибуты screen_width и screen_
# height объекта ai_settings, после чего объект ai_settings также используется для
# получения цвета фона при заполнении экрана .

# -------------------------------------------------------------------------------------------------------------------