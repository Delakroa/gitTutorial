# Знакомство с Django
#
# Современные веб-сайты в действительности представляют собой многофункциональные
# приложения, достаточно близкие к полноценным приложениям для
# настольных систем. Python содержит богатый набор инструментов для постро-
# ения веб-приложений. В этой главе вы научитесь использовать Django (http://
# djangoproject.com/) для построения проекта Learning Log — сетевой журнальной
# системы для отслеживания информации, полученной вами по определенной теме.
# Мы напишем спецификацию для этого проекта, а затем определим модели для
# данных, с которыми будет работать приложение. Мы воспользуемся администра-
# тивной системой Django для ввода некоторых начальных данных, а затем научимся
# писать представления и шаблоны, на базе которых Django будет строить страницы
# нашего сайта.
# Django представляет собой веб-инфраструктуру — набор инструментов для постро-
# ения интерактивных веб-сайтов. Django может реагировать на запросы страниц,
# упрощает чтение и запись информации в базы данных, управление пользователями
# и многие другие операции. В главах 19 и 20 мы доработаем проект Learning Log,
# а затем развернем его на сервере, чтобы вы (и ваши друзья) могли использовать их.

# --------------------------------------------------------------------------------------------------------------------

# Подготовка к созданию проекта

# В начале работы над проектом необходимо описать проект в спецификации. Затем
# вы создадите виртуальную среду для построения проекта.

# --------------------------------------------------------------------------------------------------------------------

# Написание спецификации

# В полной спецификации описываются цели проекта, его функциональность,
# а также внешний вид и интерфейс пользователя. Как и любой хороший проект
# или бизнес-план, спецификация должна сосредоточиться на самых важных аспек-
# тах и обеспечивать планомерную разработку проекта. Здесь мы не будем писать
# полную спецификацию, а сформулируем несколько четких целей, которые будут
# задавать направление процесса разработки. Вот как выглядит спецификация:
# Мы напишем веб-приложение с именем Learning Log, при помощи которого пользователь сможет
# вести журнал интересующих его тем и создавать записи в журнале во время изучения каждой
# темы. Домашняя страница Learning Log содержит описание сайта и приглашает пользователя заре-
# гистрироваться либо ввести свои учетные данные. После успешного входа пользователь получает
# возможность создавать новые темы, добавлять новые записи, читать и редактировать существующие
# записи.
# Во время изучения нового материала бывает полезно вести журнал того, что вы
# узнали, — записи пригодятся для контроля и возвращения к необходимой инфор-
# мации. Хорошее приложение повышает эффективность этого процесса.

# ------------------------------------------------------------------------------------------------------------------

# Создание виртуальной среды
#
# Для работы с Django необходимо сначала создать виртуальную среду для работы.
# Виртуальная среда представляет собой подраздел системы, в котором вы можете
# устанавливать пакеты в изоляции от всех остальных пакетов Python. Отделение
# библиотек одного проекта от других проектов принесет пользу при развертывании
# Learning Log на сервере в главе 20.
# Создайте для проекта новый каталог с именем learning_log, перейдите в этот
# каталог
# в терминальном режиме и создайте виртуальную среду. Если вы работаете
# в Python 3, то сможете создать виртуальную среду следующей командой:
# learning_log$ python -m venv ll_env
# learning_log$
# Команда запускает модуль venv и использует его для создания виртуальной среды
# с именем ll_env. Если этот способ сработал, переходите к разделу «Активизация
# виртуальной среды» на с. 382. Если что-то не получилось, прочитайте следующий
# раздел — «Установка virtualenv».

# ------------------------------------------------------------------------------------------------------------------

# Установка virtualenv
#
# Если вы используете более раннюю версию Python или ваша система не настроена
# для правильного использования модуля venv, установите пакет virtualenv. Уста-
# новка virtualenv выполняется следующей командой:
#
# $ pip install --user virtualenv
#
# Возможно, вам придется использовать слегка измененную версию этой команды.
# (Если вы еще не использовали pip, обратитесь к разделу «Установка пакетов Python
# с использованием pip» на с. 227.)
#
# ПРИМЕЧАНИЕ
# Если вы используете Linux, но и этот способ не сработал, установите virtualenv при помощи менед-
# жера пакетов своей системы. Например, в Ubuntu для установки virtualenv используется команда
# sudo apt-get install python-virtualenv.
# Перейдите в каталог learning_log в терминальном окне и создайте виртуальную
# среду следующей командой:
#
# learning_log$ virtualenv ll_env
# New python executable in ll_env/bin/python
# Installing setuptools, pip...done.
# learning_log$

# ПРИМЕЧАНИЕ
# Если в вашей системе установлено несколько версий Python, укажите версию, которая должна ис-
# пользоваться virtualenv. Например, команда virtualenv ll_env --python=python3 создаст виртуальную
# среду, которая использует Python 3.

# ------------------------------------------------------------------------------------------------------------------

# Активизация виртуальной среды
#
# После того как виртуальная среда будет создана, ее необходимо активизировать
# следующей командой:
#
# learning_log$ source ll_env/bin/activate
#  (ll_env)learning_log$
#
# Команда запускает сценарий activate из каталога ll_env/bin. Когда среда активизирует-
# ся, ее имя выводится в круглых скобках ; теперь вы можете устанавливать пакеты
# в среде и использовать те пакеты, что были установлены ранее. Пакеты, установлен-
# ные в ll_env, будут доступны только в то время, пока среда остается активной.
#
# ПРИМЕЧАНИЕ
# Если вы работаете в системе Windows, используйте команду ll_env\Scripts\activate (без слова
# source) для активизации виртуальной среды.
#
# Чтобы завершить использование виртуальной среды, введите команду deactivate:
#
# (ll_env)learning_log$ deactivate
# learning_log$
#
# Среда также становится неактивной при закрытии терминального окна, в котором
# она работает.

# ------------------------------------------------------------------------------------------------------------------

# Установка Django
#
# После того как вы создали свою виртуальную среду и активизировали ее, устано-
# вите Django:
#
# (ll_env)learning_log$ pip install Django
# Installing collected packages: Django
# Successfully installed Django
# Cleaning up...
# (ll_env)learning_log$
#
# Так как вы работаете в виртуальной среде, эта команда выглядит одинаково во всех
# системах. Использовать флаг --user не нужно, как и использовать более длинные
# команды вида python -m pip install имя_пакета.
# Помните, что с Django можно работать только в то время, пока среда остается
# активной.

# ------------------------------------------------------------------------------------------------------------------

# Создание проекта в Django

# Не выходя из активной виртуальной среды (пока ll_env выводится в круглых
# скобках), введите следующие команды для создания нового проекта:
#
#  (ll_env)learning_log$ django-admin startproject learning_log .
#  (ll_env)learning_log$ ls
# learning_log ll_env manage.py
#  (ll_env)learning_log$ ls learning_log
# __init__.py settings.py urls.py wsgi.py
#
# Команда  приказывает Django создать новый проект с именем learning_log.
# Точка в конце команды создает новый проект со структурой каталогов, которая
# упрощает развертывание приложения на сервере после завершения разработки.
#
# ПРИМЕЧАНИЕ
# Не забывайте про точку, иначе у вас могут возникнуть проблемы с конфигурацией при разверты-
# вании приложения. А если вы все же забыли, удалите созданные файлы и папки (кроме ll_env)
# и снова выполните команду.
#
# Команда ls (dir в Windows)  показывает, что Django создает новый каталог с име-
# нем learning_log. Также создается файл manage.py — короткая программа, которая
# получает команды и передает их соответствующей части Django для выполнения.
# Мы используем эти команды для управления такими задачами, как работа с базами
# данных и запуск серверов.
# В каталоге learning_log находятся четыре файла , важнейшими из которых явля-
# ются файлы settings.py, urls.py и wsgi.py. Файл settings.py определяет то, как Django
# взаимодействует с вашей системой и управляет вашим проектом. Мы изменим
# некоторые из существующих настроек и добавим несколько новых настроек в ходе
# разработки проекта. Файл urls.py сообщает Django, какие страницы следует строить
# в ответ на запросы браузера. Файл wsgi.py помогает Django предоставлять создан-
# ные файлы (имя файла является сокращением от «Web Server Gateway Interface»).


# ------------------------------------------------------------------------------------------------------------------

# Создание базы данных

# Так как Django хранит бульшую часть информации, относящейся к проекту, в базе
# данных, необходимо создать базу данных, с которой Django сможет работать. Чтобы
# создать базу данных для проекта Learning Log, введите следующую команду (все
# еще не покидая активной среды):
#
# (ll_env)learning_log$ python manage.py migrate
#  Operations to perform:
# Synchronize unmigrated apps: messages, staticfiles
# Apply all migrations: contenttypes, sessions, auth, admin
# ...
# Applying sessions.0001_initial... OK
#  (ll_env)learning_log$ ls
# db.sqlite3 learning_log ll_env manage.py
#
# Каждое изменение базы данных называется миграцией. Первое выполнение коман-
# ды migrate приказывает Django проверить, что база данных соответствует текуще-
# му состоянию проекта. Когда мы впервые выполняем эту команду в новом проекте
# с использованием SQLite (вскоре мы расскажем о SQLite более подробно), Django
# создает новую базу данных за нас. В точке  Django сообщает о создании таблиц
# базы данных, необходимых для хранения информации, используемой в проекте
#
# Synchronize unmigrated apps), а затем проверяет, что структура базы данных со-
# ответствует текущему коду (Apply all migrations).
# Выполнение команды ls показывает, что Django создает другой файл с именем
# db.sqlite3 . SQLite — база данных, работающая с одним файлом; она идеально
# подходит для написания простых приложений, потому что вам не нужно особенно
# следить за управлением базой данных.

# ------------------------------------------------------------------------------------------------------------------

# Просмотр проекта

# Убедимся в том, что проект был создан правильно. Введите команду runserver:

# (ll_env)learning_log$ python manage.py runserver
# Performing system checks...
#  System check identified no issues (0 silenced).
# July 15, 2015 - 06:23:51
#  Django version 1.8.4, using settings 'learning_log.settings'
#  Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.

# Django запускает сервер, чтобы вы могли просмотреть проект в своей системе
# и проверить, как он работает. Когда вы запрашиваете страницу, вводя URL в бра-
# узере, сервер Django отвечает на запрос; для этого он строит соответствующую
# страницу и отправляет страницу браузеру.
# В точке  Django проверяет правильность созданного проекта; в точке  выво-
# дится версия Django и имя используемого файла настроек; в точке  возвращается
# URL-адрес, по которому доступен проект. URL http://127.0.0.1:8000/ означает, что
# проект ведет прослушивание запросов на порте 8000 локального хоста (localhost),
# то есть вашего компьютера. Термином «локальный хост» обозначается сервер,
# который обрабатывает только запросы вашей системы; он не позволяет никому
# другому просмотреть разрабатываемые страницы.
# Теперь откройте браузер и введите URL http://localhost:8000/ — или
# http://127.0.0.1:8000/, если первый адрес не работает. Вы увидите нечто похожее
# на рис. 18.1 — страницу, которую создает Django, чтобы сообщить вам, что все пока
# работает правильно. Пока не завершайте работу сервера (но, когда вы захотите
# прервать ее, это можно сделать нажатием клавиш Ctrl+C).

# ПРИМЕЧАНИЕ
# Если вы получаете сообщение об ошибке «Порт уже используется», прикажите Django исполь-
# зовать другой порт; для этого введите команду python manage.py runserver 8001 и продолжайте
# перебирать номера портов по возрастанию, пока не найдете открытый порт.

# ------------------------------------------------------------------------------------------------------------------

# Начало работы над приложением

# Проект Django представляет собой группу отдельных приложений, совместная
# работа которых обеспечивает работу проекта в целом. Пока мы создадим одно
# приложение, которое будет выполнять бульшую часть работы в нашем проекте.
# Другое приложение для управления учетными записями пользователей будет до-
# бавлено в главе 19.
# К этому моменту команда runserver должна продолжать работу в терминальном
# окне, которое вы открыли ранее. Откройте новое терминальное окно (или вкладку)
# и перейдите в каталог, содержащий manage.py. Активизируйте виртуальную среду
# и выполните команду startapp:
#
# learning_log$ source ll_env/bin/activate
# (ll_env)learning_log$ python manage.py startapp learning_logs
#  (ll_env)learning_log$ ls
# db.sqlite3 learning_log learning_logs ll_env manage.py
#  (ll_env)learning_log$ ls learning_logs/
# admin.py __init__.py migrations models.py tests.py views.py
#
# Команда startapp имя_приложения приказывает Django создать инфраструктуру,
# необходимую для построения приложения. Заглянув сейчас в каталог проекта, вы
# найдете в нем новый подкаталог с именем learning_logs . Откройте этот каталог,
# чтобы увидеть, какие файлы были созданы Django . Самые важные файлы в этом
# каталоге — models.py, admin.py и views.py.
# Мы воспользуемся файлом models.py для определения данных, которыми нуж-
# но управлять в нашем приложении. К файлам admin.py и views.py мы вернемся
# позднее.

# ---------------------------------------------------------------------------------------------------------------------

# Определение моделей

# Ненадолго задумаемся, какие данные нам понадобятся. Каждый пользователь
# создает набор тем в своем журнале. Каждая запись, которую он сделает, будет при-
# вязана к определенной теме, а записи будут выводиться в текстовом виде. Также
# необходимо хранить временну́ю метку каждой записи, чтобы пользователь знал,
# когда эта запись была создана.
# Откройте файл models.py и просмотрите его текущее содержимое:
#
# models.py
# from django.db import models
#
# Модуль с именем models импортируется автоматически, и нам предлагается создать
# свои модели. Модель сообщает Django, как работать с данными, которые будут хра-
# ниться в приложении. С точки зрения кода модель представляет собой обычный
# класс; она содержит атрибуты и методы, как и все остальные классы, рассматри-
# вавшиеся нами ранее. Вот как выглядит модель тем обсуждения, которые будут
# сохраняться пользователями:
#
# from django.db import models
#
# class Topic(models.Model):
# """Тема, которую изучает пользователь"""
#  text = models.CharField(max_length=200)
#  date_added = models.DateTimeField(auto_now_add=True)
#  def __str__(self):
# """Возвращает строковое представление модели."""
# return self.text
#
# Мы создали класс с именем Topic, наследующий от Model — родительского класса,
# включенного в Django и определяющего базовую функциональность модели. Класс
# Topic содержит всего два атрибута: text и date_added.
# Атрибут text содержит данные CharField — блок данных, состоящий из символов,
# то есть текст . Атрибуты CharField могут использоваться для хранения неболь-
# ших объемов текста: имен, заголовков, названий городов и т. д. При определении
# атрибута CharField необходимо сообщить Django, сколько места нужно зарезер-
# вировать для него в базе данных. В данном случае задается максимальная длина
# max_length, равная 200 символам; этого должно быть достаточно для хранения
# большинства имен тем.
# Атрибут date_added содержит данные DateTimeField — блок данных для хранения
# даты и времени . Аргумент auto_add_now=True приказывает Django автоматически
# присвоить этому атрибуту текущую дату и время каждый раз, когда пользователь
# создает новую тему.
#
# ПРИМЕЧАНИЕ
# Полный список всех полей, которые могут использоваться в модели, приведены в документе Django
# Model Field Reference по адресу https://docs.djangoproject.com/en/1.8/ref/models/fields/. Возможно,
# вся эта информация вам сейчас не понадобится, но она будет в высшей степени полезной, когда
# вы начнете разрабатывать собственные приложения.
#
# Необходимо сообщить Django, какой атрибут должен использоваться по умолча-
# нию при вводе информации о теме. Django вызывает метод __str__() для вывода
# простого представления модели. Мы написали реализацию __str__(), которая
# возвращает строку, хранящуюся в атрибуте text .
#
# ПРИМЕЧАНИЕ
# Если вы используете Python 2.7, метод __str__() должен называться __unicode__(). Тело метода
# остается неизменным.

# ---------------------------------------------------------------------------------------------------------------------

# Активизация моделей

# Чтобы использовать модели, необходимо приказать Django включить приложение
# в общий проект. Откройте файл settings.py (из каталога learning_log/learning_log)
# и найдите в нем раздел, который сообщает Django, какие приложения установлены
# в проекте:

# settings.py
# ...
# INSTALLED_APPS = (
# 'django.contrib.admin',
# 'django.contrib.auth',
# 'django.contrib.contenttypes',
# 'django.contrib.sessions',
# 'django.contrib.messages',
# 'django.contrib.staticfiles',
# )
# ...

# Это обычный кортеж, который сообщает Django, какие приложения образуют про-
# ект. Добавьте наше приложение в этот кортеж; измените содержимое INSTALLED_
# APPS, чтобы оно выглядело так:

# ...
# INSTALLED_APPS = (
# ...
# 'django.contrib.staticfiles',
# # Мои приложения
# 'learning_logs',
# )
# ...

# Группировка приложений в проекте упрощает управление ими по мере того, как
# проект растет, а количество приложений увеличивается. Здесь мы создаем раздел,
# который пока содержит только приложение learning_logs.
# Затем необходимо приказать Django изменить базу данных для хранения инфор-
# мации, относящейся к модели Topic. В терминальном окне введите следующую
# команду:

# (ll_env)learning_log$ python manage.py makemigrations learning_logs
# Migrations for 'learning_logs':
# 0001_initial.py:
# - Create model Topic
# (ll_env)learning_log$

# По команде makemigrations Django определяет, как изменить базу данных для
# хранения информации, связанной с новыми моделями. Из результатов видно, что
# Django создает файл миграции с именем 0001_initial.py. Эта миграция создает в базе
# данных таблицу для модели Topic.
# Теперь применим миграцию для автоматического изменения базы данных:

# (ll_env)learning_log$ python manage.py migrate
# ...
# Running migrations:
# Rendering model states... DONE
#  Applying learning_logs.0001_initial... OK

# Бульшая часть вывода этой команды совпадает с выводом, полученным при первом
# выполнении команды migrate. Обратить внимание следует на строку ; здесь
# Django подтверждает, что применение миграции для learning_logs прошло успеш-
# но.
# Каждый раз, когда вы захотите изменить данные, которыми управляет Learning
# Log, выполните эти три действия: внесите изменения в models.py, вызовите
# makemigrations для learning_logs и прикажите Django выполнить миграцию про-
# екта (migrate).

# ------------------------------------------------------------------------------------------------------------------

# Административный сайт Django

# Django позволяет легко работать с моделями, определенными для приложения,
# через административный сайт. Этот сайт используется администраторами сайта,
# а не рядовыми пользователями. В этом разделе мы создадим административный
# сайт и используем его для добавления некоторых тем через модель Topic.

# Создание суперпользователя
# Django позволяет создать пользователя, обладающего полным набором привилегий
# на сайте; такой пользователь называется суперпользователем. Привилегии управля-
# ют действиями, которые разрешено выполнять пользователю. На самом жестком
# уровне привилегий пользователь может только читать общедоступную информа-
# цию на сайте. Зарегистрированным пользователям обычно предоставляется при-
# вилегия чтения своих приватных данных, а также избранной информации, доступ-
# ной только для участников сообщества. Для эффективного администрирования
# веб-приложения владельцу сайта обычно должна быть доступна вся информация,
# хранящаяся на сайте. Хороший администратор внимательно относится к конфи-
# денциальной информации пользователя, потому что пользователи доверяют тем
# приложениям, с которыми они работают.
# Чтобы создать суперпользователя в Django, введите следующую команду и от-
# ветьте на запросы:

# (ll_env)learning_log$ python manage.py createsuperuser
#  Username (leave blank to use 'ehmatthes'): ll_admin
#  Email address:
#  Password:
# Password (again):
# Superuser created successfully.
# (ll_env)learning_log$

# При получении команды createsuperuser Django предлагает ввести имя пользо-
# вателя, который является суперпользователем . Здесь мы вводим имя ll_admin,
# но вы можете ввести любое имя на свое усмотрение. Также можно ввести адрес
# электронной почты или оставить это поле пустым . После этого следует дважды
# ввести пароль .

# ПРИМЕЧАНИЕ
# Часть конфиденциальной информации может быть скрыта от администраторов сайта. Например,
# Django на самом деле не сохраняет введенный пароль; вместо этого сохраняется хеш — специ-
# альная строка, построенная на основе пароля. И когда в будущем вы вводите пароль, Django снова
# хеширует введенные данные и сравнивает результат с хранимым хешем. Если два хеша совпадают,
# то проверка пройдена. Если же хакер в результате атаки получит доступ к базе данных сайта, он
# сможет прочитать только хранящийся в базе хеш, но не пароли. При правильной настройке сайта
# восстановить исходные пароли из хешей почти невозможно.

# Регистрация модели на административном сайте

# Django добавляет некоторые модели (например, User и Group) на административ-
# ный сайт автоматически, но модели, которые мы создали, придется регистрировать
# вручную.
# При запуске приложения learning_logs Django создает файл admin.py в одном
# каталоге с models.py:

# admin.py
# from django.contrib import admin
# # Зарегистрируйте здесь ваши модели.
# Чтобы зарегистрировать Topic на административном сайте, введите следующую
# команду:
# from django.contrib import admin
#  from learning_logs.models import Topic
#  admin.site.register(Topic)

# Этот код импортирует модель Topic , после чего использует вызов admin.site.
# register() , регистрирующий модель для управления через административный
# сайт.
# Теперь используйте учетную запись суперпользователя для входа на администра-
# тивный сайт. Введите адрес http://localhost:8000/admin/, введите имя пользователя
# и пароль для только что созданного суперпользователя, и вы увидите экран напо-
# добие изображенного на рис. 18.2. На этой странице можно добавлять новых поль-
# зователей и группы, а также вносить изменения в уже существующие настройки.
# Помимо этого можно работать с данными, связанными с только что определенной
# моделью Topic.

# ПРИМЕЧАНИЕ
# Если в браузере появляется сообщение о недоступности веб-страницы, убедитесь в том, что сервер
# Django работает в терминальном окне. Если сервер не работает, активизируйте виртуальную среду
# и снова введите команду python manage.py runserver.

# Добавление тем
# Когда модель Topic зарегистрирована на административном сайте, добавим
# первую тему. Щелкните на ссылке Topics, чтобы перейти к странице Topics; стра-
# ница практически пуста, потому что еще нет ни одной темы для выполнения
# операций. Щелкните на ссылке Add; открывается форма для добавления новой
# темы. Введите в первом поле текст Chess и щелкните на ссылке Save. Вы воз-
# вращаетесь к административной странице Topics, на которой появляется только
# что созданная тема.
# Создадим вторую тему, чтобы у вас было больше данных для работы. Снова щелкните
# на ссылке Add и создайте вторую тему Rock Climbing. Ссылка Save снова воз-
# вращает вас к основной странице Topics, где отображаются обе темы, Chess и Rock
# Climbing.

# --------------------------------------------------------------------------------------------------------------------

# Определение модели Entry

# Чтобы сохранить информацию о том, что вы узнали по этим двум темам, необходимо
# определить модель для записей, которые пользователь делает в своих журна-
# лах. Каждая запись должна ассоциироваться с конкретной темой. Такое отношение
# называется отношением «многие-к-одному», поскольку многие записи могут быть
# связаны с одной темой.

# Код модели Entry выглядит так:

# models.py
# from django.db import models
# class Topic(models.Model):
# ...
#  class Entry(models.Model):
# """Информация, изученная пользователем по теме"""
#  topic = models.ForeignKey(Topic)
#  text = models.TextField()
# date_added = models.DateTimeField(auto_now_add=True)
#  class Meta:
# verbose_name_plural = 'entries'
# def __str__(self):
# """Возвращает строковое представление модели."""
#  return self.text[:50] + "..."

# Класс Entry наследует от базового класса Model, как и рассмотренный ранее класс
# Topic . Первый атрибут, topic, является экземпляром ForeignKey . Термин
# «внешний ключ» (foreign key) происходит из теории баз данных; внешний ключ со-
# держит ссылку на другую запись в базе данных. Таким образом каждая запись свя-
# зывается с конкретной темой. Каждой теме при создании присваивается ключ, или
# идентификатор. Если потребуется установить связь между двумя записями данных,
# Django использует ключ, связанный с каждым блоком информации. Вскоре мы
# используем такие связи для получения всех записей, связанных с заданной темой.
# Затем идет атрибут с именем text, который является экземпляром TextField .
# Полю такого типа ограничение размера не требуется, потому что размер отдельных
# записей не ограничивается. Атрибут date_added позволяет отображать записи в по-
# рядке их создания и снабдить каждую запись временной меткой.
# В точке  класс Meta вкладывается в класс Entry. Класс Meta хранит дополнитель-
# ную информацию по управлению моделью; в данном случае он позволяет задать
# специальный атрибут, который приказывает Django использовать форму мно-
# жественного числа Entries при обращении более чем к одной записи. (Без этого
# Django будет использовать неправильную форму Entrys.) Наконец, метод __str__()
# сообщает Django, какая информация должна отображаться при обращении к от-
# дельным записям. Так как запись может быть достаточно длинным блоком текста,
# мы приказываем Django выводить только первые 50 символов . Также добавля-
# ется многоточие — признак вывода неполного текста.

# --------------------------------------------------------------------------------------------------------------------

# Миграция модели Entry   392