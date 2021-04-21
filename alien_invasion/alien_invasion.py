import sys

import pygame

from settings import Settings


def run_game():
    """Инициализирует игру и создаёт объект экрана."""
    # Инициализирует pygame, settings и обьект экрана.
    pygame.init()
    ai_settings = Settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Назначение цвета фона.
    bg_color = (230, 230, 230)
    # Запуск основного цикла игры.

    while True:
        # При каждом прохождение цикла перерисовывается экран.
        screen.fill(ai_settings.bg_color)
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()
