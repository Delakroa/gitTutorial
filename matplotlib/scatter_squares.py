import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)
# Назначение заголовка диагрыммы и меток осей.
plt.title("Номер квадрата", fontsize=24)  # .title подписать загаловок.
plt.xlabel("Значения", fontsize=14)  # Подписать ось Х.
plt.ylabel("Значение квадрата", fontsize=14) # Подписать ось y.

# Назначение размера шрифта на осях.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
