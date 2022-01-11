import sys
import random
import winsound
import requests
import time
import numpy as np
import mss.tools
import os.path
from datetime import date
import keyboard
import mouse
# установочное имя для трех следующих библиотек pywin32
from win32gui import GetWindowText, GetForegroundWindow
import win32api
import win32con


# привязка телеграм бота к питону
# нужно в телеграмме зайти в канал BotFather
# там написать сообщение /newbot
# дать имя своему каналу например MSWordPrint
# потом дать имя своему боту который будет сидеть в этом канале например MSWordPrint_bot (окончание _bot обязательно)
# потом зайти в созданный канал и нажать кнопку START
# потом в обычном броузере перейти по адресу как ниже указано
# https://api.telegram.org/bot' + bot_token + '/getUpdates'
# и посмотреть свой chatID
def telegram_bot_sendtext(bot_message):
    # имя говорящего конретного этого а не другого бота
    name_bot = ' 🐘 '

    bot_token = ''
    bot_chatID = ''

    bot_token_atas = ''
    bot_chatID_atas = ''

    # задать АЛАРМ слово, если в сообщении есть это слово, то сообщение продублируется на другой канал
    e = 'АТАС'

    bot_message = str(time.asctime()[11:-8]) + name_bot + ' ' + bot_message

    if len(bot_token + bot_chatID + bot_token_atas + bot_chatID_atas) != 0:
        send_text = 'https://api.telegram.org/bot' + \
                    bot_token + \
                    '/sendMessage?chat_id=' + \
                    bot_chatID + \
                    '&parse_mode=Markdown&text=' + \
                    bot_message

        requests.get(send_text)

        if e in bot_message:
            send_text = 'https://api.telegram.org/bot' + \
                        bot_token_atas + \
                        '/sendMessage?chat_id=' + \
                        bot_chatID_atas + \
                        '&parse_mode=Markdown&text=' + \
                        bot_message
            requests.get(send_text)
        return


# подсчет процента прочности удочки
def pole_durability():
    # задать совсем белый цвет BGR
    real_white = np.array([255, 255, 255], dtype=np.uint8)
    # считать кусок экрана
    # save_chunk_screen(monitor_pole_durability)
    monitor_pole_durability_array = np.array(mss.mss().grab(monitor_pole_durability), dtype=np.uint8)[:, :, 0:3]
    # длина белой полоски в пикселях
    len_white = 177
    for i in range(len_white, 1, -3):
        if (monitor_pole_durability_array[2, i] == real_white).all():
            res = int(i // (len_white / 100))
            return res
    telegram_bot_sendtext('Или удочка только что была починена.' +
                          ' Или сообщение о ДТ.' +
                          ' Или глюк игры - исчез фрейм удочки в нижнем правом углу.' +
                          ' даю две табуляции')
    sleep(1)
    keyboard.press_and_release('tab')
    sleep(1)
    keyboard.press_and_release('tab')
    sleep(1)
    if if_f3_is_ready():
        # если кнопка F3 видна, значит правая кнопка мыши помогла
        telegram_bot_sendtext('вижу F3 после починки или исчезновения фрейма')
    else:
        keyboard.press_and_release('F3')
        telegram_bot_sendtext('нажал F3 после починки или исчезновения фрейма')
        sleep(2)
    return 100


# функция починки удочки в
def pole_repair():
    telegram_bot_sendtext('🛠 Починка удочки')
    sleep(2)
    # табуляция открыть окно эквипа
    keyboard.press_and_release('tab')
    sleep(2)
    # переместить мышку на удочку
    mouse.move(870, 660, absolute=True)
    sleep(0.5)
    # дать клик
    mouse.click(button='left')
    sleep(2)
    # переместить мышку на меню починки
    mouse.move(960, 660, absolute=True)
    sleep(0.5)
    # дать клик
    mouse.click(button='left')
    sleep(2)
    # переместить мышку на меню починки удочки без бафоф
    mouse.move(960, 700, absolute=True)
    sleep(0.5)
    # дать клик
    mouse.click(button='left')
    sleep(2)
    # нажать Е
    keyboard.press_and_release('e')
    sleep(0.5)
    # закрыть окно эквипа табуляцией
    keyboard.press_and_release('tab')
    sleep(2)
    # вернуть ловлю рыбки после починки однократным нажатием F3
    keyboard.press_and_release('F3')
    sleep(2)
    return


# проверить что F3 отображается
def if_f3_is_ready():
    # считать кусок экрана
    # save_chunk_screen(monitor_f3)
    monitor_f3_array = np.array(mss.mss().grab(monitor_f3), dtype=np.uint8)[:, :, 0:3]
    if pix_white_or_no(monitor_f3_array[9, 9]) and \
            pix_black_or_no(monitor_f3_array[9, 13]) and \
            pix_white_or_no(monitor_f3_array[9, 17]):
        return True
    if pix_white_or_no(monitor_f3_array[10, 8]) and \
            pix_black_or_no(monitor_f3_array[10, 14]) and \
            pix_white_or_no(monitor_f3_array[10, 18]):
        return True

    return False


# проверка что поплавок находится в нижнем правом углу
def if_float_down():
    # сделать скрин нижнего поплавка
    # save_chunk_screen(monitor_float)
    monitor_float_array = np.array(mss.mss().grab(monitor_float), dtype=np.uint8)[:, :, 0:3]
    if pix_white_or_no(monitor_float_array[2, 1]) and \
            pix_black_or_no(monitor_float_array[4, 7]) and \
            pix_white_or_no(monitor_float_array[8, 17]):
        return True
    else:
        return False


# правильная функция точной задержки. например: sleep(0.002) - две тысячные одной секунды
def sleep(duration, get_now=time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        if flag_stop:
            return
        now = get_now()


# проверяет пиксель светлый или нет
def pix_white_or_no(pix):
    # если все из BGR выше 190 будем считать пиксель светлым
    if pix[0] > 190 and pix[1] > 190 and pix[2] > 190:
        return True
    return False


# проверяет пиксель темный или нет
def pix_black_or_no(pix):
    # если все из BGR меньше 12 будем считать пиксель темным
    if pix[0] < 12 and pix[1] < 12 and pix[2] < 12:
        return True
    return False


# функция сохранения кусков экрана
def save_chunk_screen(def_monitor):
    with mss.mss() as sct:
        sct_img = sct.grab(def_monitor)
        fname = (full_path
                 + 'Screen/screen_'
                 + str(time.time())
                 + ("_{top}x{left}_{width}x{height}".format(**def_monitor))
                 + '.png')
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=fname)


# флаг сохранения экрана

# найти ДВА наиболее близких друг к другу делителя чьё произведение равно
# произведению ТРЕХ заданных положительных чисел
def find_mlt_xy(mlt_xy):
    # в любом варианте число делится на себя и на единицу
    min_x = mlt_xy
    min_y = 1
    # ищем другие варианты перебором
    for i in range(mlt_xy):
        # если остаток от деления (операция "%") равен нолю, то у нас деление без остатка
        if (mlt_xy % (i + 1)) == 0:
            # делим по модулю, точно зная что остатка не будет
            y = (mlt_xy // (i + 1))
            # если сумма двух множителей меньше предыдудущей суммы минимумов
            if (y + (i + 1)) < min_x:
                # то присвоить новый минимум сумм
                min_x = (y + (i + 1))
                min_y = i + 1
    # делим по модулю, точно зная что остатка не будет
    min_x = mlt_xy // min_y
    # если надо, то разворачиваем размеры так чтобы результат был широким, а не стоял столбиком как в тик-токе
    if min_x < min_y:
        tmp_min_x = min_y
        min_y = min_x
        min_x = tmp_min_x
    return min_x, min_y


# смещение заброса по X Y
move_d_x = 0
# переменная зависания скрипта
time_stuck = time.time()
# общее количество рыбок за сессию
fish_count_session = 0

full_path = 'Resourse/' + str(date.today()) + '/'
os.makedirs(full_path + "Screen/", exist_ok=True)

# флаг выхода из программы
flag_stop = False
# флаг создания скринов для отладки
flag_screen = False
# флаг начала рыбалки
fishing_run = False
# сколько раз забросили в асфальт
asphalt_count = 0
# сколько раз бездействовал
stun_count = 0
# прочность удочки на старте скрипоат
pole_durability_count = 100
# флаг подтверждения что поплавок находится в нижнем правом углу
float_down = False
# флаг подтверждения подсечки рыбы
flag_hook = False
# отпустить кнопку alt
keyboard.release('alt')
mouse.release(button='left')
mouse_down = False
# флаг помогающий незнающему програмисту
fuflo = False


# флаг остановки скрипта
def key_space():
    global flag_stop
    flag_stop = True


def key_f2():
    # сохраняем много скринов всего экрана
    # повторное нажатие останавливает сохранение скринов
    global flag_screen
    if flag_screen:
        flag_screen = False
        winsound.Beep(500, 300)
    else:
        winsound.Beep(2500, 300)
        flag_screen = True


# регистрируем события
keyboard.on_press_key('F2', lambda event: key_f2(), suppress=False)
keyboard.on_press_key(' ', lambda event: key_space(), suppress=False)

# задать координаты квадрата "F3"
monitor_f3 = {"left": 1048, "top": 801, "width": 24, "height": 20}
# задать координаты тестового куска экрана
monitor_test = {"left": 1674, "top": 858, "width": 223, "height": 126}
# задать координаты поплавка в нижнем правом углу
monitor_float = {"left": 1818, "top": 930, "width": 20, "height": 14}
# задать координаты буквы 'H' в слове HOOK когда поплавок в нижнем правом углу
monitor_hook = {"left": 1874, "top": 944, "width": 38, "height": 23}
# полный размер монитора
monitor_all = {"left": 0, "top": 0, "width": 1920, "height": 1080}
# прочность удочки
monitor_pole_durability = {"left": 1689, "top": 1032, "width": 179, "height": 5}

# ======================================================
# ЗАПУСК ОСНОВНОГО ТЕЛА СКРИПТА
# ======================================================
# создаем директорию для сохранения скринов, даже если она существует

print("RUN ...")
winsound.Beep(800, 100)
# послать в телеграм сообщени о начале новой сессии
telegram_bot_sendtext('====== новая сессия ======')
sleep(0.2)

while True:
    # выход
    if flag_stop:
        winsound.Beep(800, 100), winsound.Beep(800, 100), winsound.Beep(800, 100)
        print("DONE !!!")
        # отпустить кнопку alt
        keyboard.release('alt')
        mouse.release(button='left')
        sys.exit()

    # если активное окно не игра, то цикл while начинается заново
    if GetWindowText(GetForegroundWindow()) != "New World":
        # подождать и пойти на следующий цикл "while True:"
        sleep(0.2)
        continue

    # если установлен флаг сохранения экрана
    if flag_screen:
        # то сохранить экран
        save_chunk_screen(monitor_all)
        continue

    # проверка на зависание ПЕРВАЯ - поплавок после начала вываживания ушел в сторону
    if (time.time() - time_stuck) > 30:
        # итерация счетчика бездействия
        stun_count += 1
        telegram_bot_sendtext('👩‍🎓  30 секунд бездействия - ' +
                              str(stun_count) +
                              ' подряд')
        # поднять все зажимы
        fish_count_session = fish_count_session - 1
        keyboard.release('alt')
        mouse.release(button='left')
        mouse.release(button='right')
        # погасить все флаги разных действий рыбалки
        fishing_run = False
        float_down = False
        flag_hook = False
        time_stuck = time.time()
        telegram_bot_sendtext(' 👩‍🎓  поднял все флаги')
        # вернуть направление взгляда в исходное по оси X
        for move in range(move_d_x):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, 0, 0, 0)
            sleep(0.001)
        telegram_bot_sendtext(' 👩‍🎓  вернул взгляд по оси X')

        # пробуем найти удочку
        if if_f3_is_ready():
            # если кнопка F3 видна, значит бросили в камень.
            telegram_bot_sendtext('👩‍🎓  вижу F3')
        else:
            # нажать правую кномпку мышки, чтобы появилась F3
            mouse.release(button='right')
            sleep(0.2)
            mouse.click(button='right')
            sleep(2)
            telegram_bot_sendtext('👩‍🎓  нажал правую кнопку мыши')
            if if_f3_is_ready():
                # если кнопка F3 видна, значит правая кнопка мыши помогла
                telegram_bot_sendtext('👩‍🎓  вижу F3')
            else:
                keyboard.press_and_release('F3')
                sleep(2)
                telegram_bot_sendtext('👩‍🎓  нажал F3')
                if if_f3_is_ready():
                    # если кнопка F3 видна, значит помогла F3 после правай кнопки мыши
                    telegram_bot_sendtext('👩‍🎓  вижу F3')
                else:
                    # если кнопка F3 все еще не видна, попробовать отремонтировать удочку
                    telegram_bot_sendtext('👩‍🎓  запускаю блок ремонта удочки')
                    pole_repair()
                    sleep(2)
                    if if_f3_is_ready():
                        telegram_bot_sendtext('👩‍🎓  вижу F3 после ремонта удочки')
                    else:
                        keyboard.press_and_release('F3')
                        telegram_bot_sendtext('👩‍🎓  нажал F3 после ремонта удочки')
                        if if_f3_is_ready():
                            telegram_bot_sendtext('👩‍🎓  вижу F3 после ремонта удочки + F3')
        continue

    # ЧЕТВЕРТОЕ: если произошла подсечка рыбы, начинаем отпускать мышку пока на поплавке есть не черное
    if flag_hook:
        # сделать скрин поплавка
        monitor_float_scan = np.array(mss.mss().grab(monitor_float), dtype=np.uint8)[:, :, 0:3]
        # если все черные пиксели наместе
        if pix_black_or_no(monitor_float_scan[7, 9]) and \
                pix_black_or_no(monitor_float_scan[9, 12]) and \
                pix_black_or_no(monitor_float_scan[12, 16]):
            # проверить нажата ли сейчас мышка
            if mouse_down:
                # то все в порядке
                fuflo = True
            else:
                # значит нужно нажать мышку и установить флаг мышки
                # print(str(time.time()) + ' все черные на месте, но мышка была не нажата, нажал мышку')
                mouse.press(button='left')
                mouse_down = True
                time_stuck = time.time()
        else:
            # если не все черные на месте и нет коромысла, видимо поплавок изчез,
            # save_chunk_screen(monitor_test)
            # save_chunk_screen(monitor_float)
            if pix_white_or_no(monitor_float_scan[1, 1]) and pix_black_or_no(monitor_float_scan[1, 2]):
                # если не все черные на месте, но коромысло наместе все еще, то
                # мы увидели всполохи
                # отпустить мышку и подождать три секунды
                # чтобы не порвалась леска
                mouse.release(button='left')
                mouse_down = False
                # print(str(time.time()) + ' обнаружил пружинку, отпустил мышку на 2 секунды')
                sleep(2 + (random.randint(-20, 20) / 100))
                time_stuck = time.time()
            else:
                # значит окончилась рыбалка, тем или иным способом, и нужно погасить флаг подсечки
                flag_hook = False
                # и освободить нажатие мышки
                mouse.release(button='left')
                mouse_down = False
                # print(str(time.time()) + ' наверное поплавок изчес, окончил вывождение рыбки')
                fish_count_session = fish_count_session + 1
                # save_chunk_screen(monitor_all)
                time_stuck = time.time()
        continue

    # ТРЕТЬЕ: если поплавок в нижнем правом углу, начинаем ждать букву Н в слове HOOK, и подсекаем когда дождались
    if float_down:
        # сделать скрин места буквы Н
        # save_chunk_screen(monitor_hook)
        monitor_f3_array = np.array(mss.mss().grab(monitor_hook), dtype=np.uint8)[:, :, 0:3]
        if pix_white_or_no(monitor_f3_array[5, 26]) and \
                pix_black_or_no(monitor_f3_array[5, 5]) and \
                pix_white_or_no(monitor_f3_array[16, 34]):
            # подсечь рыбку
            float_down = False
            flag_hook = True
            mouse.press(button='left')
            sleep(2 + (random.randint(-20, 20) / 100))
            mouse_down = True
            time_stuck = time.time()
        continue

    # ПЕРВОЕ: сделать скрин квадрата "F3"
    # забросить удочку если на экране "F3"
    if if_f3_is_ready():
        # поднять флаг заброса удочки
        fishing_run = True
        # отпустить кнопку alt
        keyboard.release('alt')
        # дать нормальное время на анимацию возврата взгляда после альта
        sleep(0.5)
        # вернуть направление взгляда в исходное по оси X
        for move in range(move_d_x):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, 0, 0, 0)
            sleep(0.01)
        sleep(0.5)
        # сгенерировать новое смещение X от 100 до 500
        move_d_x = random.randint(20, 40)
        # немного сместить заброс по оси X
        for move in range(move_d_x):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 0, 0, 0)
            sleep(0.01)
        # дать нормальное время на анимацию поворота взгляда
        sleep(0.2)
        # проверить исправность удочки, если недавно не было ремонта
        pole_durability_count = pole_durability()
        telegram_bot_sendtext('прочность ' + str(pole_durability_count) + '%' + ' / поймал: ' + str(fish_count_session))
        if pole_durability_count < 25:
            # починить удочку
            pole_repair()
        sleep(0.2)
        # зажать кнопку alt
        keyboard.press('alt')
        # зажать левую мышку
        mouse.press(button='left')
        # дать на заброс около двух секунд
        sleep(2 + (random.randint(-20, 20) / 100))
        # отпустить мышку
        mouse.release(button='left')
        # добавить на полет поплавка около двух секунд
        sleep(2 + (random.randint(-20, 20) / 100))
        # print(str(time.time()) + ' закинул удочку')
        # пойти на следующий цикл "while True:"
        time_stuck = time.time()
        continue

    # ВТОРОЕ: если забросили удочку, повернуть камеру и проверить что поплавок оказался в углу
    if fishing_run:
        # всегда опускаем флаг начала рыбалки (заброс может быть только один)
        fishing_run = False
        # некое непонятное время на движение мышки
        move_speed = 750
        for move in range(move_speed):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, -1, 0, 0)
            sleep(0.001)
        # добавить на отрисовку поплавка пару секунд
        sleep(0.5 + (random.randint(-20, 20) / 100))
        # если поплавок обнаружен на своём месте
        if if_float_down():
            # поплавок на месте
            # передать управление в блок подсекания
            float_down = True
            # выполнено удачное действие - обнуляем таймер зависания
            time_stuck = time.time()
            # выполнено удачное действие - обнуляем таймер бросков в асфальт
            asphalt_count = 0
        else:
            # поплавок не найден на нужном месте
            # попытки перезапуска рыбался
            # 1 проверить если присутствует на экране F3 значит был бросок не в воду
            asphalt_count += 1
            telegram_bot_sendtext('🚗 Попытка найти поплавок после заброса ' +
                                  str(asphalt_count) +
                                  ' раза подряд')
            # пробуем перезабросить удочку
            sleep(2)
            if if_f3_is_ready():
                # если кнопка F3 видна, значит бросили в камень.
                telegram_bot_sendtext('👀 ничего не делал, вижу F3')
            else:
                # нажать правую кномпку мышки, чтобы появилась F3
                mouse.click(button='right')
                telegram_bot_sendtext('🚗 нажал правую кнопку мыши')
                sleep(2)
                if if_f3_is_ready():
                    # если кнопка F3 видна, значит правая кнопка мыши помогла
                    telegram_bot_sendtext('👀 вижу F3 после правой кнопки')
                else:
                    keyboard.press_and_release('F3')
                    telegram_bot_sendtext('🚗 нажал F3')
                    sleep(2)
                    if if_f3_is_ready():
                        # если кнопка F3 видна, значит помогла F3 после правай кнопки мыши
                        telegram_bot_sendtext('👀 вижу F3 после правой кнопки и F3')
                    else:
                        keyboard.press_and_release('F3')
                        telegram_bot_sendtext('🚗 нажал F3 второй раз')
                        sleep(2)
                        if if_f3_is_ready():
                            # если кнопка F3 видна, значит помогла вторая F3 после одной правай кнопки мыши
                            telegram_bot_sendtext(
                                '👀 вижу F3 после правой кнопки и двух F3')
                        else:
                            telegram_bot_sendtext('🚗 не смог найти F3 после потери поплавка')
            if asphalt_count > 3:
                # уже больше пяти раз подряд бросаем мимо воды
                telegram_bot_sendtext('🚗 🚗 🚗 АТАС - четыре раз подряд бросаем мимо воды.')
                sleep(2)
                keyboard.release('alt')
                sleep(2)
                for i in range(200):
                    sleep(123.4 + (random.randint(-600, 600) / 100))
                    telegram_bot_sendtext('🚗 🚗 🚗 АТАС ' +
                                          str(20 - i) +
                                          ' сделайте со мной: [ctrl+F2]')
                    sleep(2)
                    keyboard.press_and_release('tab')
                    sleep(2)
                telegram_bot_sendtext('🚗 🚗 🚗 Скрипт остановлен!')
                sleep(0.2)
                save_chunk_screen(monitor_all)
                flag_stop = True
        continue

    # хорошая задержка
    sleep(0.2)

    # тестовый останов
    # sys.exit()
