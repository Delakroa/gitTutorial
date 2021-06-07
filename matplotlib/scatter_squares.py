import matplotlib.pyplot as plt

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

# Назначение заголовка диагрыммы и меток осей.
plt.title("Номер квадрата", fontsize=24)  # .title подписать загаловок.
plt.xlabel("Значения", fontsize=14)  # Подписать ось Х.
plt.ylabel("Значение квадрата", fontsize=14) # Подписать ось y.

# Назначение диапазона для каждой оси.
plt.axis([0, 1100, 0, 1100000])

# Назначение размера шрифта на осях.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
