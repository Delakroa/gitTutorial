# Ведение счета

# В этой главе построение игры Alien Invasion будет завершено. Мы добавим
# кнопку Play для запуска игры по желанию игрока или перезапуска игры после
# ее завершения. Мы также изменим игру, чтобы она ускорялась при переходе
# игрока на следующий уровень, и реализуем систему подсчета очков. К концу
# главы вы будете знать достаточно, чтобы заняться разработкой игр, сложность
# которых нарастает по ходу игры и в которых реализована система подсчета
# очков.

# -------------------------------------------------------------------------------------------------------------------

# Добавление кнопки Play

# В этом разделе мы добавим кнопку Play, которая отображается перед началом игры
# и появляется после ее завершения, чтобы игрок мог сыграть снова.
# В текущей версии игра начинается сразу же после запуска alien_invasion.py. После
# очередных изменений игра будет запускаться в неактивном состоянии и предла-
# гать игроку нажать кнопку Play для запуска. Для этого включите следующий код
# в game_stats.py:

# game_stats.py
#
# def __init__(self, ai_settings):
# """Инициализирует статистику."""
# self.ai_settings = ai_settings
# self.reset_stats()
# # Игра запускается в неактивном состоянии.
# self.game_active = False
# def reset_stats(self):
# ...
#
# Итак, программа запускается в неактивном состоянии, а игру можно запустить
# только нажатием кнопки Play.

# --------------------------------------------------------------------------------------------------------------------

# Создание класса Button

# Так как в Pygame не существует встроенного метода создания кнопок, мы напишем
# класс Button для создания заполненного прямоугольника с текстовой надписью.
# Следующий код может использоваться для создания кнопок в любой игре. Ниже
# приведена первая часть класса Button; сохраните ее в файле button.py:

# button.py
#
# import pygame.font
#
# class Button():
#
#  def __init__(self, ai_settings, screen, msg):
# """Инициализирует атрибуты кнопки."""
# self.screen = screen
# self.screen_rect = screen.get_rect()
# # Назначение размеров и свойств кнопок.
#  self.width, self.height = 200, 50
# self.button_color = (0, 255, 0)
# self.text_color = (255, 255, 255)
#  self.font = pygame.font.SysFont(None, 48)
# # Построение объекта rect кнопки и выравнивание по центру экрана.
#  self.rect = pygame.Rect(0, 0, self.width, self.height)
# self.rect.center = self.screen_rect.center
# # Сообщение кнопки создается только один раз.
#  self.prep_msg(msg)

# Сначала программа импортирует модуль pygame.font, который позволяет Pygame
# выводить текст на экран. Метод __init__() получает параметры self, объекты
# ai_settings и screen, а также строку msg с текстом кнопки . Размеры кнопки
# задаются в точке , после чего атрибуты button_color и text_color задаются так,
# чтобы прямоугольник кнопки был окрашен в ярко-зеленый цвет, а текст выводился
# белым цветом.
# В точке  происходит подготовка атрибута font для вывода текста. Аргумент None
# сообщает Pygame, что для вывода текста должен использоваться шрифт по умолча-
# нию, а значение 48 определяет размер текста. Чтобы выровнять кнопку по центру
# экрана, мы создаем объект rect для кнопки  и задаем его атрибут center в соот-
# ветствии с одноименным атрибутом экрана.
# Pygame выводит строку текста в виде графического изображения. В точке  эта
# задача решается методом prep_msg(). Код prep_msg() выглядит так:

# button.py
#
# def prep_msg(self, msg):
# """Преобразует msg в прямоугольник и выравнивает текст по центру."""
#  self.msg_image = self.font.render(msg, True, self.text_color,
# self.button_color)
#  self.msg_image_rect = self.msg_image.get_rect()
# self.msg_image_rect.center = self.rect.center

# Метод prep_msg() должен получать параметр self и текст, который нужно вы-
# вести в графическом виде (msg). Вызов font.render() преобразует текст, храня-
# щийся в msg, в изображение, которое затем сохраняется в msg_image . Методу
# font.render() также передается логический признак режима сглаживания текста.
# В остальных аргументах передаются цвет шрифта и цвет фона. В нашем примере
# режим сглаживания включен (True), а цвет фона совпадает с цветом фона кнопки.
# (Если цвет фона не указан, Pygame пытается вывести шрифт с прозрачным фоном.)
# В точке  изображение текста выравнивается по центру кнопки, для чего создается
# объект rect изображения, а его атрибут center приводится в соответствие с одно-
# именным атрибутом кнопки.
# Остается создать метод draw_button(), который может вызываться для отображе-
# ния кнопки на экране:

# button.py
#
# def draw_button(self):
# # Отображение пустой кнопки и вывод сообщения.
# self.screen.fill(self.button_color, self.rect)
# self.screen.blit(self.msg_image, self.msg_image_rect)

# Вызов метода screen.fill() рисует прямоугольную часть кнопки. Затем вызов
# screen.blit() выводит изображение текста на экран с передачей изображения
# и объекта rect, связанного с изображением. Класс Button готов.

# --------------------------------------------------------------------------------------------------------------------

# Вывод кнопки на экран

# В программе класс Button используется для создания кнопки Play. Так как нам
# нужна только одна кнопка Play, мы создадим кнопку прямо в файле alien_invasion.py:

# alien_invasion.py
#
# ...
# from game_stats import GameStats
# from button import Button
# ...
# def run_game():
# ...
# pygame.display.set_caption("Alien Invasion")
# # Создание кнопки Play.
#  play_button = Button(ai_settings, screen, "Play")
# ...
# # Запуск основного цикла игры.
# while True:
# ...
#  gf.update_screen(ai_settings, screen, stats, ship, aliens,
# bullets,
# play_button)
#
# run_game()

# Программа импортирует класс Button и создает экземпляр play_button , после
# чего передает play_button функции update_screen(), чтобы кнопка появлялась
# при обновлении экрана .
# Затем следует внести изменения в update_screen(), чтобы кнопка Play появлялась
# только в неактивном состоянии игры:

# game_functions.py
#
# def update_screen(ai_settings, screen, stats, ship, aliens, bullets,
# play_button):
# """Обновляет изображения на экране и отображает новый экран."""
# ...
# # Кнопка Play отображается в том случае, если игра неактивна.
# if not stats.game_active:
# play_button.draw_button()
# # Отображение последнего прорисованного экрана.
# pygame.display.flip()

# Чтобы кнопка Play не закрывалась другими элементами экрана, мы отображаем
# ее после всех остальных игровых элементов, но перед переключением на новый
# экран. Теперь при запуске Alien Invasion в центре экрана отображается кнопка
# Play (рис. 14.1).

# --------------------------------------------------------------------------------------------------------------------

# Запуск игры
#
# Чтобы при нажатии кнопки Play запускалась новая игра, добавьте в файл game_
# functions.py следующий код для отслеживания событий мыши над кнопкой:
#
# game_functions.py
#
# def check_events(ai_settings, screen, stats, play_button, ship, bullets):
# """Обрабатывает нажатия клавиш и события мыши."""
# for event in pygame.event.get():
# if event.type == pygame.QUIT:
# ...
#  elif event.type == pygame.MOUSEBUTTONDOWN:
#  mouse_x, mouse_y = pygame.mouse.get_pos()
#  check_play_button(stats, play_button, mouse_x, mouse_y)
# def check_play_button(stats, play_button, mouse_x, mouse_y):
# """Запускает новую игру при нажатии кнопки Play."""
#  if play_button.rect.collidepoint(mouse_x, mouse_y):
# stats.game_active = True

# Обновленное определение check_events() получает параметры stats и play_button.
# Параметр stats будет использоваться для обращения к флагу game_active, а play_
# button — для проверки того, была ли нажата кнопка Play.
# Pygame обнаруживает событие MOUSEBUTTONDOWN, когда игрок щелкает в любой точке
# экрана , но мы хотим ограничить игру, чтобы она реагировала только на щелчки
# на кнопке Play. Для этого будет использоваться метод pygame.mouse.get_pos(),
# возвращающий кортеж с координатами x и y точки щелчка . Эти значения пере-
# даются функции check_play_button() , которая использует метод collidepoint()
# для проверки того, находится ли точка щелчка в пределах области, определяемой
# прямоугольником кнопки Play . Если точка находится в пределах кнопки, флаг
# game_active переводится в состояние True, и игра начинается!
# При вызове check_events() в alien_invasion.py должны передаваться два дополни-
# тельных аргумента, stats и play_button:

# alien_invasion.py
#
# # Запуск основного цикла игры.
# while True:
# gf.check_events(ai_settings, screen, stats, play_button, ship,
# bullets)
# ...
#
# К этому моменту вы сможете запустить и сыграть полноценную игру. После за-
# вершения игры значение game_active становится равным False, а кнопка Play снова
# появится на экране.

# -------------------------------------------------------------------

