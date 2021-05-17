import pygame.font


class Scoreboard:
    """Класс для вывода игровой информации."""

    def __init__(self, ai_settings, screen, stats):
        """Инициализирует атрибуты подсчёта очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Настройка шрифта для вывода счёта.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Подготовка исходного изображения.
        self.prep_score()

    def prep_score(self):
        """Преобразует текущий счёт в графическое изображение."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self, text_color, self.ai_settings.bg_color)

        # Выводит счёт в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Выводит счёт на экран."""
        self.screen.blit(self.score_image, self.score_rect)
