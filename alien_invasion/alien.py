import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузите изображение пришельца и установите его атрибут rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Запускайте каждого нового пришельца в верхнем левом углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции пришельца.
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца"""                  # Отрисовка выполняется с помощью метода blit
        self.screen.blit(self.image, self.rect)  # (можно создавать дополнительные поверхности)

    # def check_edges(self):
    #     """Верните True, если пришелец находится на краю экрана."""
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.right >= screen_rect.right or self.rect.left <= 0:
    #         return True
    #
    # def update(self):
    #     """Переместите инопланетянина вправо или влево."""
    #     self.x += (self.settings.alien_speed * self.settings.fleet_direction)
    #     self.rect.x = self.x
