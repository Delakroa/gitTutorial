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

