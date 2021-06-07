from random import choice


class RandomWalk:
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_points=5000):
        """Инициализация атрибутов блуждания"""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0).
        self.x_value = [0]
        self.y_value = [0]
