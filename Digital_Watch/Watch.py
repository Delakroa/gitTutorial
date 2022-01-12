import sys
from tkinter import *
import time


# создайте функцию синхронизации и переменную current_time
def timing():
    # отображать текущий часов, минут, секунд
    current_time = time.strftime("%H : %M : %S")
    # настроить часы
    clock.config(text=current_time)
    # часы будут меняться каждые 200 микросекунд
    clock.after(200, timing)


# Создайте переменную, в которой будет храниться наше окно tkinter.
root = Tk()
# определить размер окна
root.geometry("600x300")
# создать переменные часы и сохранить метку
# Первая метка покажет время, вторая метка покажет час:минуту:секунду, третья метка покажет верхние цифровые часы.
clock = Label(root, font=("times", 60, "bold"), bg="white")
clock.grid(row=2, column=2, pady=25, padx=100)
timing()

# создать переменную для цифровых часов
digital = Label(root, text="Цифровые часы для А.Н. Камызина", font="times 24 bold")
digital.grid(row=0, column=2)

nota = Label(root, text="Час        минуты        секунды", font="times 15 bold")
nota.grid(row=3, column=2)

root.mainloop()



# def flash(button):
#     current_color = button.cget("background")
#     next_color = "green" if current_color == "red" else "red"
#     button.config(background=next_color)
#     root.after(1000, flash, button)