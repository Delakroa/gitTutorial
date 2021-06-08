import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новое блуждания строятся до тех пор, пока программа остается активной.
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk()
    rw.fill_walk()
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=15)
    # Выделение первой и последней точки.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=100)

    # Удаление осей.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Сделайте еще одну Random Walk? (y/n): ")
    if keep_running == 'n':
        break
