import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)
# Назначение заголовка диагрыммы и меток осей.
plt.title("Номер квадрата", fontsize=24)
plt.xlabel("Значения", fontsize=14)
plt.ylabel("Значение квадрата", fontsize=14)

# Назначение размера шрифта на осях.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
