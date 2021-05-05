# В этой главе в игру Alien Invasion будут добавлены пришельцы. Сначала мы добавим одного пришельца
# у верхнего края экрана, а потом сгенерируем целый
# флот. Пришельцы будут перемещаться в сторону и вниз; при этом пришельцы,
# в которых попадают пули, исчезают с экрана. Наконец, мы ограничим количество кораблей у игрока,
# так что при гибели последнего корабля игра завершается.
# В этой главе вы узнаете больше о Pygame и о ведении крупного проекта. Вы
# также научитесь обнаруживать коллизии (столкновения) игровых объектов,
# например пуль и пришельцев. Обнаружение коллизий помогает определять
# взаимодействия между элементами игры: например, ограничить перемещение
# персонажа областью между стенами лабиринта или организовать передачу мяча
# между двумя персонажами. Работа будет продолжаться на основе плана, к которому мы будем время от времени возвращаться,
# чтобы не отклоняться от цели
# во время написания кода.
# Итак, прежде чем браться за новый код для добавления флота пришельцев на экран,
# рассмотрим проект и обновим план.

# Анализ проекта

# Приступая к новой фазе разработки крупного проекта, всегда полезно вернуться
# к исходному плану и уточнить, чего же вы хотите добиться в том коде, который
# собираетесь написать. В этой главе мы:
#  Проанализируем код и определим, нужно ли провести рефакторинг перед реализацией новых возможностей.
#  Добавим в левом верхнем углу экрана одного пришельца, отделив его от краев
# экрана интервалами.
#  По величине интервалов вокруг первого пришельца и общим размерам экрана
# вычислим, сколько пришельцев поместится на экране. Для создания пришельцев, заполняющих верхнюю часть экрана, будет
# написан цикл.
#  Организуем перемещение флота пришельцев в сторону и вниз, пока весь флот
# не будет уничтожен, пока пришелец не столкнется с кораблем игрока или пока
# пришелец не достигнет земли. Если весь флот будет уничтожен, программа
# создает новый флот. Если пришелец сталкивается с кораблем или с землей,
# программа уничтожает корабль и создает новый флот.Создание пришельца 257
#  Ограничим количество кораблей, которые могут использоваться игроком, и завершим игру в конце последней попытки.
# Этот план будет уточняться по мере реализации новых возможностей, но для начала и этого достаточно.
# Также проводите анализ кода, когда вы начинаете работу над новой серией возможностей проекта. Так как с каждой
# новой фазой проект обычно становится
# более сложным, лучше всего заняться расчисткой излишне громоздкого или неэффективного кода. И хотя сейчас особой
# расчистки не потребуется, потому что
# мы уже проводили промежуточный рефакторинг, необходимость использовать
# мышь для закрытия игры каждый раз, когда потребуется протестировать новую
# функцию, раздражает. Добавим возможность быстрого завершения игры при нажатии клавиши Q:

# game_functions.py

# def check_keydown_events(event, ai_settings, screen, ship, bullets):
# ...
# elif event.key == pygame.K_q:
# sys.exit()
# В check_keydown_events() добавляется новый блок, который завершает игру при
# нажатии клавиши Q. Это довольно безопасное изменение, потому что клавиша Q
# находится достаточно далеко от клавиш со стрелками и пробела, так что вероятность случайного нажатия Q и
# завершения игры невелика. Теперь при тестировании игру можно закрыть клавишей Q, не прибегая к использованию мыши.

# --------------------------------------------------------------------------------------------------------------------

# Создание пришельца
#
# Размещение одного пришельца на экране мало чем отличается от размещения
# корабля. Поведением каждого пришельца будет управлять класс с именем Alien,
# который по своей структуре очень похож на класс Ship. Для простоты мы снова воспользуемся готовыми
# графическими изображениями. Вы можете найти

# Создание класса Alien
#
# Теперь можно написать класс Alien:
#
# alien.py
#
# import pygame
# from pygame.sprite import Sprite
# class Alien(Sprite):
# """Класс, представляющий одного пришельца."""
# def __init__(self, ai_settings, screen):
# """Инициализирует пришельца и задает его начальную позицию."""
# super(Alien, self).__init__()
# self.screen = screen
# self.ai_settings = ai_settings
# # Загрузка изображения пришельца и назначение атрибута rect.
# self.image = pygame.image.load('images/alien.bmp')
# self.rect = self.image.get_rect()
# # Каждый новый пришелец появляется в левом верхнем углу экрана.
# 	 self.rect.x = self.rect.width
# self.rect.y = self.rect.height
# # Сохранение точной позиции пришельца.
# self.x = float(self.rect.x)
# def blitme(self):
# """Выводит пришельца в текущем положении."""
# self.screen.blit(self.image, self.rect)

# В основном этот класс похож на класс Ship (если не считать размещения пришельца).
# Изначально каждый пришелец размещается в левом верхнем углу экрана, при
# этом слева от него добавляется интервал, равный ширине пришельца, а над ним —
# интервал, равный высоте 

# -------------------------------------------------------------------------------------------------------------------

# Создание экземпляра Alien

# Создадим экземпляр Alien в alien_invasion py:
# alien_invasion.py
# ...
# from ship import Ship
# from alien import Alien
# import game_functions as gf

# def run_game():
# ...
# # Создание пришельца.
# alien = Alien(ai_settings, screen)
# # Запуск основного цикла игры.
# while True:
# gf.check_events(ai_settings, screen, ship, bullets)
# ship.update()
# gf.update_bullets(bullets)
# gf.update_screen(ai_settings, screen, ship, alien, bullets)
# run_game()

# Программа импортирует новый класс Alien и создает экземпляр Alien непосред-
# ственно перед входом в основной цикл while. Так как позиция пришельца еще
# не успела измениться, ничего нового в цикле не добавляется; изменения вносятся
# только в вызов update_screen(), которому передается экземпляр alien.

# -------------------------------------------------------------------------------------------------------------------

# Отображение пришельца на экране

# Чтобы пришелец появился на экране, программа вызывает его метод blitme()
# в update_screen():

# game_functions.py

# def update_screen(ai_settings, screen, ship, alien, bullets):
#     """При каждом прохождение цикла перерисовывается экран."""
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#     alien.blitme()
#
#     # Все пули выводятся позади изображения корабля и пришельцев.
#     for bullet in bullets.sprites():
#         bullet.draw_bullet()

# Отображение последнего прорисованного экрана.
# pygame.display.flip()

# Пришелец выводится после прорисовки корабля и пуль, так что пришельцы будут
# находиться на верхнем «слое» экрана. На рис. 13.2 изображен первый пришелец.
# После того как первый пришелец появится на экране, мы напишем код для вывода
# всего флота.

# --------------------------------------------------------------------------------------------------------------------

# Построение флота

# Чтобы нарисовать флот пришельцев, необходимо вычислить, сколько пришельцев
# поместится в одном ряду и сколько рядов поместится по высоте. Сначала мы вы-
# числим горизонтальные интервалы между пришельцами и создадим ряд; затем
# будет вычислен вертикальный интервал и создан весь флот.

# Вычисление количества пришельцев в одном ряду

# Чтобы определить, сколько пришельцев помещается в одном ряду, сначала вы-
# числим доступное горизонтальное пространство. Ширина экрана хранится в ai_
# settings.screen_width, но с обеих сторон экрана необходимо зарезервировать
# пустые интервалы. Определим их равными ширине одного пришельца. Так как
# ширина уменьшается на величину двух интервалов, доступное пространство равно
# ширине экрана за вычетом удвоенной ширины пришельца:
# available_space_x = ai_settings.screen_width — (2 * alien_width)
# Также необходимо зарезервировать интервалы между пришельцами; они будут со-
# ставлять одну ширину пришельца. Пространство, необходимое для вывода одного
# пришельца, равно его удвоенной ширине: одна ширина для самого пришельца и еще
# одна для пустого интервала справа. Чтобы определить количество пришельцев на
# экране, разделим доступное пространство на удвоенную ширину пришельца:
# number_aliens_x = available_space_x / (2 * alien_width)
# Эти вычисления будут включены в программу при создании флота.

# ПРИМЕЧАНИЕ
# У вычислений в программировании есть одна замечательная особенность: не обязательно быть
# полностью уверенным в правильности формулы, когда вы ее пишете. Вы можете опробовать
# формулу на практике и посмотреть, что из этого получится. В худшем случае получится экран,
# до отказа
# забитый пришельцами, — или наоборот, пустой. В этом случае вы пересмотрите формулу
# на основании полученных результатов.

# --------------------------------------------------------------------------------------------------------------

# Создание ряда
#
# Чтобы создать один ряд пришельцев, сначала создадим в alien_invasion.py пустую
# группу с именем aliens для хранения всех пришельцев, а затем вызовем функцию
# в game_functions.py для создания флота:
# alien_invasion.py
#
# import pygame
#
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# import game_functions as gf
# def run_game():
# ...
# # Создание корабля, группы пуль и группы пришельцев.
# ship = Ship(ai_settings, screen)
# bullets = Group()
#  aliens = Group()
# # Создание флота пришельцев.
#  gf.create_fleet(ai_settings, screen, aliens)
# # Запуск основного цикла игры.
# while True:
# ...
#  gf.update_screen(ai_settings, screen, ship, aliens,
# bullets)
# run_game()
#
# Так как пришельцы уже не создаются напрямую в alien_invasion.py, импортировать
# класс Alien в этот файл не обязательно.
# Создайте пустую группу для хранения всех пришельцев в игре . Затем создайте
# новую функцию create_fleet() , которую мы вскоре вызовем, и передайте ей
# ai_settings, объект screen и пустую группу aliens. Затем измените вызов update_
# screen(), чтобы предоставить функции доступ к группе пришельцев .
# Также необходимо внести изменения в update_screen():
#
# game_functions.py
#
# def update_screen(ai_settings, screen, ship, aliens, bullets):
# ...
# ship.blitme()
# aliens.draw(screen)
# # Отображение последнего прорисованного экрана.
# pygame.display.flip()
# Когда вы вызываете метод draw() для группы, Pygame автоматически выводит
# каждый элемент группы в позиции, определяемой его атрибутом rect. В дан-
# ном случае вызов aliens.draw(screen) рисует каждого пришельца в группе
# на экране.

# ---------------------------------------------------------------------------------------------------------------------

# Создание флота

# Теперь можно перейти к созданию флота. Ниже приведена новая функция create_
# fleet(), которую мы поместим в конец game_functions.py. Также необходимо
# импортировать класс Alien, не забудьте добавить команду import в начало файла:

# game_functions.py
#
# ...
# from bullet import Bullet
# from alien import Alien
# ...
# def create_fleet(ai_settings, screen, aliens):
# """Создает флот пришельцев."""
# # Создание пришельца и вычисление количества пришельцев в ряду.
# # Интервал между соседними пришельцами равен одной ширине пришельца.
#  alien = Alien(ai_settings, screen)
#  alien_width = alien.rect.width
#  available_space_x = ai_settings.screen_width - 2 * alien_width
#  number_aliens_x = int(available_space_x / (2 * alien_width))
# # Создание первого ряда пришельцев.
#  for alien_number in range(number_aliens_x):
# # Создание пришельца и размещение его в ряду.
#  alien = Alien(ai_settings, screen)
# alien.x = alien_width + 2 * alien_width * alien_number
# alien.rect.x = alien.x
# aliens.add(alien)

# Бульшая часть этого кода уже была описана ранее. Для размещения пришельцев
# необходимо знать ширину и высоту одного пришельца, и мы создаем его в точке 
# перед выполнением вычислений. Этот пришелец не войдет во флот, поэтому он не
# включается в группу aliens. В точке  ширина пришельца определяется по его
# атрибуту rect, а полученное значение сохраняется в alien_width, чтобы избежать
# лишних обращений к атрибуту rect. В точке  вычисляется горизонтальное про-
# странство и количество пришельцев, которые в нем поместятся.
# По сравнению с исходными формулами всего одно изменение: мы используем
# int(), чтобы вычисленное количество пришельцев  было целым, — во-первых,
# неясно, что делать с неполным пришельцем, а во-вторых, функция range() должна
# получать целое число. Функция int() отсекает дробную часть числа, фактически
# выполняя округление в меньшую сторону. (И это правильно: лучше оставить лиш-
# нее свободное место в каждом ряду, чем забивать ряды до отказа.)
# Затем создается цикл от 0 до количества создаваемых пришельцев . В теле цикла
# создается новый пришелец, после чего задается его координата x для размещения
# его в ряду . Каждый пришелец сдвигается вправо на одну ширину от левого поля.
# Затем ширина пришельца умножается на 2, чтобы учесть полное пространство,
# выделенное для одного пришельца, включая пустой интервал справа, а получен-
# ная величина умножается на позицию пришельца в ряду. Затем новый пришелец
# добавляется в группу aliens.

# Запустив программу Alien Invasion, вы увидите, что на экране появился первый
# ряд пришельцев (рис. 13.3).
# Первый ряд сдвинут влево, и это хорошо, потому что флот пришельцев должен дви-
# гаться вправо, пока не дойдет до края экрана, затем немного опуститься вниз, затем
# двигаться влево и т. д. Как и в классической игре Space Invaders, такое перемещение
# интереснее, чем постепенное снижение по прямой. Движение будет продолжаться
# до тех пор, пока все пришельцы не будут сбиты или пока пришелец не столкнется
# с кораблем или нижним краем экрана.
#
# ПРИМЕЧАНИЕ
# В зависимости от выбранной ширины экрана расположение первого ряда пришельцев в вашей
# системе может выглядеть немного иначе.

# ---------------------------------------------------------------------------------------------------------------------

# Рефакторинг create_fleet()

# Если бы создание флота на этом было завершено, то функцию create_fleet(),
# пожалуй, можно было бы оставить в таком виде, но работа еще не закончена, по-
# этому мы немного подчистим код функции. Ниже приведена версия create_fleet()
# с двумя новыми функциями: get_number_aliens_x() и create_alien():

# game_functions.py

#  def get_number_aliens_x(ai_settings, alien_width):
# """Вычисляет количество пришельцев в ряду."""
# available_space_x = ai_settings.screen_width - 2 * alien_width
# number_aliens_x = int(available_space_x / (2 * alien_width))
# return number_aliens_x
# def create_alien(ai_settings, screen, aliens, alien_number):
# """Создает пришельца и размещает его в ряду."""
# alien = Alien(ai_settings, screen)
#  alien_width = alien.rect.width
# alien.x = alien_width + 2 * alien_width * alien_number
# alien.rect.x = alien.x
# aliens.add(alien)
#
# def create_fleet(ai_settings, screen, aliens):
# """Создает флот пришельцев."""
# # Создание пришельца и вычисление количества пришельцев в ряду.
# alien = Alien(ai_settings, screen)
#  number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
#
# # Создание первого ряда пришельцев.
# for alien_number in range(number_aliens_x):
#  create_alien(ai_settings, screen, aliens, alien_number)

# Код get_number_aliens_x() нисколько не изменился по сравнению с create_
# fleet() . Код create_alien() почти не изменился, разве что для определения ши-
# рины используется только что созданный пришелец . В точке  код вычисления
# горизонтальных интервалов заменяется вызовом get_number_aliens_x(), а строка
# с alien_width удалена, потому что теперь задача решается в create_alien(). В точ-
# ке  вызывается функция create_alien(). Рефакторинг упрощает добавление
# новых строк и создание всего флота.

# --------------------------------------------------------------------------------------------------------------------

# Добавление рядов

# Чтобы завершить построение флота, определите количество рядов на экране
# и повторите цикл (создания пришельцев одного ряда) полученное количество
# раз. Чтобы определить количество рядов, мы вычисляем доступное вертикаль-
# ное пространство, вычитая высоту пришельца (сверху), высоту корабля (снизу)
# и удвоенную
# высоту пришельца (снизу):
# available_space_y = ai_settings.screen_height — 3 * alien_height — ship_height
# В результате вокруг корабля образуется пустое пространство, чтобы у игрока было
# время начать стрельбу по пришельцам в начале каждого уровня. Под каждым рядом
# должно быть пустое место, равное высоте пришельца. Чтобы вычислить количество
# строк, мы делим свободное пространство на удвоенную высоту пришельца (как
# и прежде, если формула содержит ошибку, мы это немедленно увидим и внесем
# изменения, пока не получим нужные интервалы):

# number_rows = available_height_y / (2 * alien_height)

# Зная количество рядов во флоте, мы можем повторить код создания ряда:

# game_functions.py

#  def get_number_rows(ai_settings, ship_height, alien_height):
"""Определяет количество рядов, помещающихся на экране."""
#  available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
# number_rows = int(available_space_y / (2 * alien_height))
# return number_rows

# def create_alien(ai_settings, screen, aliens, alien_number, row_number):
# ...
# alien.x = alien_width + 2 * alien_width * alien_number
# alien.rect.x = alien.x
#  alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
# aliens.add(alien)

# def create_fleet(ai_settings, screen, ship, aliens):
# ...
# number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
# number_rows = get_number_rows(ai_settings, ship.rect.height,
# alien.rect.height)

# Создание флота пришельцев.
#  for row_number in range(number_rows):
# for alien_number in range(number_aliens_x):
# create_alien(ai_settings, screen, aliens, alien_number,
# row_number)

# Чтобы вычислить количество рядов, помещающихся на экране, мы включаем вы-
# числения available_space_y и number_rows в функцию get_number_rows() , похо-
# жую на get_number_aliens_x(). Вычисления заключаются в круглые скобки, чтобы
# их можно было разбить на две строки длиной 79 символов и менее, как указано
# в рекомендациях . Функция int() используется для того, чтобы предотвратить
# создание неполного ряда пришельцев.
# Чтобы создать несколько строк, мы используем два вложенных цикла: внешний
# и внутренний . Внутренний цикл создает один ряд пришельцев. Внешний цикл
# считает от 0 до количества рядов; Python использует код создания одного ряда
# и повторяет его number_rows раз.
# Чтобы создать вложенный цикл, напишите новый цикл for и снабдите повторя-
# емый код отступом. (В большинстве текстовых редакторов операции создания
# и удаления блоков кода выполняются просто, но, если вам понадобится помощь,
# обращайтесь к приложению Б.) Затем при вызове create_alien() передается
# аргумент с номером ряда, чтобы каждый ряд находился на экране ниже преды-
# дущих.
# Определению create_alien() необходим параметр с номером ряда. В create_
# alien() мы изменяем координату y пришельца. Сначала прибавляется одна
# высота пришельца, чтобы создать пустое место у верхнего края экрана. Каждый
# новый ряд начинается на две высоты пришельца ниже последнего ряда, поэтому
# мы умножаем высоту пришельца на 2, а затем на номер ряда. Номер первого ряда
# равен 0, так что вертикальное расположение первого ряда остается неизменным.
# Все последующие ряды размещаются ниже на экране.
# Определение create_fleet() также содержит новый параметр для объекта ship;
# следовательно, в вызов create_fleet() в alien_invasion.py необходимо добавить
# аргумент ship:

# alien_invasion.py

# Создание флота пришельцев.
# gf.create_fleet(ai_settings, screen, ship, aliens)
# Если теперь запустить игру, вы увидите целый флот пришельцев (рис. 13.4).
# В следующем разделе мы приведем флот в движение.

# ------------------------------------------------------------------------------------------------------------------

# Перемещение флота

# Флот пришельцев должен двигаться вправо по экрану, пока не дойдет до края;
# тогда флот опускается на заданную величину и начинает двигаться в обратном
# направлении. Это продолжается до тех пор, пока все пришельцы не будут сбиты,
# один из них не столкнется с кораблем или не достигнет низа экрана. Начнем с пере-
# мещения флота вправо.

# Перемещение вправо

# Чтобы корабли пришельцев перемещались по экрану, мы воспользуемся методом
# update() из alien.py, который будет вызываться для каждого пришельца в группе.
# Сначала добавим настройку для управления скоростью каждого пришельца:

# settings.py

# def __init__(self):
# ...
# # Настройки пришельцев
# self.alien_speed_factor = 1

# Настройка используется в реализации update():

# alien.py

# def update(self):
# """Перемещает пришельца вправо."""
#  self.x += self.ai_settings.alien_speed_factor
#  self.rect.x = self.x

# При каждом обновлении позиции пришельца мы смещаем его вправо на величину,
# хранящуюся в alien_speed_factor. Точная позиция пришельца хранится в атрибу-
# те self.x, который может принимать вещественные значения . Затем значение
# self.x используется для обновления позиции прямоугольника пришельца .
# В основном цикле while уже содержатся вызовы обновления корабля и пуль. Те-
# перь необходимо также обновить позицию каждого пришельца:

# alien_invasion.py

# Запуск основного цикла игры.
# while True:
# gf.check_events(ai_settings, screen, ship, bullets)
# ship.update()
# gf.update_bullets(bullets)
# gf.update_aliens(aliens)
# gf.update_screen(ai_settings, screen, ship, aliens, bullets)

# Позиции пришельцев обновляются после обновления пуль, потому что скоро мы
# будем проверять, попали ли какие-либо пули в пришельцев.
# Наконец, добавьте новую функцию update_aliens() в конец файла game_functions.py:

# game_functions.py
# def update_aliens(aliens):
# """Обновляет позиции всех пришельцев во флоте."""
# aliens.update()

# Мы используем метод update() для группы aliens, что приводит к автоматиче-
# скому вызову метода update() каждого пришельца. Если запустить Alien Invasion
# сейчас, вы увидите, как флот двигается вправо и исчезает за краем экрана.

# -------------------------------------------------------------------------------------------------------------------

# Создание настроек для направления флота

# Теперь мы создадим настройки, которые перемещают флот вниз по экрану, а потом
# влево при достижении правого края экрана. Вот как реализуется это поведение:
#
# settings.py
#
# # Настройки пришельцев
# self.alien_speed_factor = 1
# self.fleet_drop_speed = 10
# # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
# self.fleet_direction = 1

# Настройка fleet_drop_speed управляет величиной снижения флота при дости-
# жении им края. Эту скорость полезно отделить от горизонтальной скорости при-
# шельцев, чтобы эти две скорости можно было изменять независимо.
# Для настройки fleet_direction можно использовать текстовое значение (напри-
# мер, 'left' или 'right'), но, скорее всего, в итоге придется использовать набор
# команд if-elif для проверки направления. Так как в данном случае направлений
# всего два, мы используем значения 1 и –1 и будем переключаться между ними при
# каждом изменении направления флота. (Числа в данном случае особенно удобны,
# потому что при движении вправо координата x каждого пришельца должна увели-
# чиваться, а при перемещении влево — уменьшаться.)

# --------------------------------------------------------------------------------------------------------------------
