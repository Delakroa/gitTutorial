import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# Назначение загаловка диагрыммы и меток осей.
plt.title("Квадратные числа", fontsize=24)
plt.xlabel("Значение", fontsize=14)
plt.ylabel("Значение Квадрата", fontsize=14)
# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', labelsize=14)
plt.show()
