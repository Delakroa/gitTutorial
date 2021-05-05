import sys
from bullet import Bullet
import pygame
from alien import Alien


def chek_keydown_events(event, settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает пулю, если максимум ещё не достигнут."""
    # Создание новой пули и включение ее в группы bullets.
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def chek_keyup_events(event, ship):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:  # Модуль event для обработки очереди событий
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chek_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            chek_keydown_events(event, ai_settings, screen, ship, bullets)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """При каждом прохождение цикла перерисовывается экран."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Когда вы вызываете метод draw() для группы, Pygame автоматически выводит каждый
    # элемент группы в позиции, определяемой его атрибутом rect
    aliens.draw(screen)

    # Все пули выводятся позади изображения корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()


def update_bullets(bullets):
    """Обновляет позиции пуль и удаляет старые пули."""
    # Обновление позиции пуль
    bullets.update()

    # Удаление пуль вышедших за экран
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets)) # Проверка на кол-во пуль

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()


def get_number_aliens(ai_settings, alien_width):
    """Вычисление пришельцев"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    """Создание пришельца и размещает его в ряду."""
    alien = Alien(ai_settings, screen)  # Создание пришельцев и размер его ряда.
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """Создаёт флот пришельцев."""
    # Создаёт пришельцев и вычисление количества пришельцев в ряду
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)

    # Создание первого ряда пришельцев.
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)
