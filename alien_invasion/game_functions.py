import sys
from bullet import Bullet
import pygame


def chek_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает пулю, если максимум ещё не достигнут."""
    # Создание новой пули и включение ее в группы bullets.
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def chek_keyup_events(event, ship):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:
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


def update_screen(ai_settings, screen, ship, bullets):
    # При каждом прохождение цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
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
    # print(len(bullets))
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
