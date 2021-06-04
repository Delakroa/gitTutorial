import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Общий класс для управления игровыми активами и поведением"""

    def __init__(self):
        """Инициализирует игру и создаёт объект экрана."""
        # Инициализирует pygame, settings и обьект экрана.
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Создание экземпляра GameStats и Scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Создание коробля, групп пуль и группы пришельцев.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Создание флота пришельцев
        self._create_fleet()

        # Создание кнопки Play
        self.play_button = Button(self, "Play")

    def run_game(self):
        # Запуск основного цикла игры.
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Отвечайте на нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Начать новую игру, когда игрок нажимает кнопку "Играть"."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Сбросить настройки игры.
            self.settings.initialize_dynamic_settings()

            # Сбросить статистику игры.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Избавьтесь от всех оставшихся пришельцев и пуль.
            self.aliens.empty()
            self.bullets.empty()

            # Создайте новый флот и центрируйте корабль.
            self._create_fleet()
            self.ship.center_ship()

            # Скрыть курсор мыши.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Отвечайте на нажатия клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Отвечает на ключевые релизы."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создайте новую марку и добавьте ее в группу маркеров."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновите положение пуль и избавьтесь от старых пуль."""
        # Обновить позиции маркеров.
        self.bullets.update()

        # Избавьтесь от исчезнувших пуль.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Реагируйте на столкновения пули с инопланетянами."""
        # Удалите все пули и столкнувшиеся пришельцы..
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Уничтожьте существующие патроны и создайте новый флот.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Повышение уровня.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """
        Проверьте, находится ли флот на границе,
        затем обновите позиции всех пришельцев во флоте..
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Ищите столкновения инопланетных кораблей.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Ищите пришельцев, попадающих в нижнюю часть экрана..
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Проверьте, достигли ли инопланетяне нижней части экрана.."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Относитесь к этому так же, как если бы корабль попал.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Реагируйте на корабль, сбитый инопланетянином."""
        if self.stats.ships_left > 0:
            # Уменьшите значение ships_left и обновите табло.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Избавьтесь от оставшихся пришельцев и пуль.
            self.aliens.empty()
            self.bullets.empty()

            # Создайте новый флот и центрируйте корабль.
            self._create_fleet()
            self.ship.center_ship()

            # Пауза.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Создайте флот инопланетян."""
        # Создайте инопланетянина и найдите количество пришельцев подряд.
        # Расстояние между каждым пришельцем равно ширине одного пришельца..
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Определите количество рядов пришельцев, которые умещаются на экране.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создайте полный флот инопланетян.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создайте инопланетянина и поместите его в ряд."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Отвечайте соответствующим образом, если какие-либо инопланетяне достигли края."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Отбросьте весь флот и измените направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Обновите изображения на экране и перейдите на новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Нарисуйте информацию о счете.
        self.sb.show_score()

        # Нарисуйте кнопку воспроизведения, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Создайте экземпляр игры и запустите игру.
    ai = AlienInvasion()
    ai.run_game()
