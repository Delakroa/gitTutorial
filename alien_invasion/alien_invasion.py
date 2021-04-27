import pygame
from pygame.sprite import Group
# import sys
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    """Инициализирует игру и создаёт объект экрана."""
    # Инициализирует pygame, settings и обьект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание коробля.
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль.
    bullet = Group()
    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, ship, bullet)
        ship.update()
        bullet.update()
        # Удаление пуль вышедших за экран
        for bullet in bullet.copy():
            if bullet.rect.bottom <= 0:
                bullet.remove(bullet)
        print(len(bullet))

        gf.update_screen(ai_settings, screen, ship, bullet)


run_game()
