import matplotlib.pyplot as plt

# 15-1. Кубы: число, возведенное в третью степень, называется «кубом». Нанесите на диа-
# грамму первые пять кубов, а затем первые 5000 кубов.
# 15-2. Цветные кубы: примените цветовую карту к диаграмме с кубами.

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=60)

# Загаловок диаграммы и метки осей
plt.title("Задание 15-1", fontsize=24)
plt.xlabel('Значения X', fontsize=14)
plt.ylabel('Значение **3', fontsize=14)

# Назначение размера шрифта на осях.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
