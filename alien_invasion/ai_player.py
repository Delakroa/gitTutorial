import pygame

from alien_invasion import AlienInvasion


class AIPlayer:

    def __init__(self, ai_game):
        """Автоматический игрок для Alien Invasion."""
        # Нужна ссылка на игровой объект.
        self.ai_game = ai_game

    def run_game(self):
        """Заменяет исходный run_game (), поэтому мы можем вставлять наши собственные
        элементы управления.
        """
        # Начните в активном состоянии и скройте мышь.
        self.ai_game.stats.game_active = True
        pygame.mouse.set_visible(False)

        # Запустить основной цикл игры.
        while True:
            # По-прежнему вызываем ai_game._check_events (), поэтому мы можем использовать клавиатуру для выхода.
            # Также вызываем наш собственный метод для инициирования событий.
            self.ai_game._check_events()
            self._implement_strategy()

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()

            self.ai_game._update_screen()

    def _implement_strategy(self):
        """Реализуйте автоматизированную стратегию игры."""
        self._sweep_right_left()

        # По возможности стреляйте пулей.
        self.ai_game._fire_bullet()

    def _sweep_right_left(self):
        """Непрерывно прокручивайте корабль вправо и влево."""
        ship = self.ai_game.ship
        screen_rect = self.ai_game.screen.get_rect()

        if not ship.moving_right and not ship.moving_left:
            # Корабль еще не двинулся; двигаться вправо.
            ship.moving_right = True
        elif (ship.moving_right and ship.rect.right > screen_rect.right - 10):
            # Корабль вот-вот ударится по правому краю; двигай влево.
            ship.moving_right = False
            ship.moving_left = True
        elif ship.moving_left and ship.rect.left < 10:
            ship.moving_left = False
            ship.moving_right = True


if __name__ == '__main__':
    ai_game = AlienInvasion()

    ai_player = AIPlayer(ai_game)
    ai_player.run_game()
