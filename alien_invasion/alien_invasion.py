import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship


# from alien import Alien


def run_game():
    """Инициализирует игру и создаёт объект экрана."""
    # Инициализирует pygame, settings и обьект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание коробля, групп пуль и группы пришельцев.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Создание пришельца
    # alien = Alien(ai_settings, screen)

    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        gf.check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


run_game()
