import pygame

from pygame.sprite import Sprite


class Ship(Sprite):
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Загрузите изображение корабля и получите его прямоугольник.
        self.rect.midbottom = self.screen_rect.midbottom

        # Каждый новый корабль появляется в центре нижнего края экрана.
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учётом флага."""
        # Обновляется атрибуты center, не rect (обькты rect для хранения и манипулирования прямоугольными областями)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление обьекта rect на self.center.
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещение корабля в центре нижней стороны """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

