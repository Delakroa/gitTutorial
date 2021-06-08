import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Построение случайного блуждания и нанесение точек на диаграмму.
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_value, rw.y_value, s=15)
plt.show()
