import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления пулями, выпущенными кораблём"""

    def __init__(self, ai_game):
        """Создаёт обьект пули в текущей позиции корабля."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Создание пули в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиция пули хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает пулю вверх по экрану."""
        # Обновление позиции пули в вещественном формате.
        self.y -= self.settings.bullet_speed
        # Обновление пзиции прямоугольника.
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)

# Для переделки
