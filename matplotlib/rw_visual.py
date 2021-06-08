import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новое блуждания строятся до тех пор, пока программа остается активной.
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk()
    rw.fill_walk()
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()
    keep_running = input("Сделайте еще одну Random Walk? (y/n): ")
    if keep_running == 'n':
        break
