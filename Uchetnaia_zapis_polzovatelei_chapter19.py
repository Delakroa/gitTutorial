# Что является самым главным для веб-приложения? Что любой пользователь, жи-
# вущий в любой стране мира, сможет создать учетную запись в вашем приложении
# и начать работать с ним. В этой главе мы построим формы, на которых пользова-
# тели смогут вводить свои темы и записи, а также редактировать существующие
# данные. Кроме того, вы узнаете, как Django защищает приложения от распростра-
# ненных атак на страницы с формами, чтобы вам не приходилось тратить много
# времени на продумывание средств защиты вашего приложения.
# Затем будет реализована система проверки пользователей. Мы создадим стра-
# ницу регистрации, на которой пользователи смогут создавать учетные записи,
# и ограничим доступ к некоторым страницам для анонимных пользователей. Затем
# некоторые функции представления будут изменены так, чтобы пользователь мог
# видеть только свои собственные данные. Вы узнаете, как обеспечить безопасность
# и конфиденциальность данных пользователей.

# --------------------------------------------------------------------------------------------------------------------

# Редактирование данных

# Прежде чем строить систему аутентификации пользователей для создания учетных
# записей, сначала мы добавим несколько страниц, на которых пользователи смогут
# вводить собственные данные. У пользователей появится возможность создавать
# новые темы, добавлять новые записи и редактировать записи, сделанные ранее.
# В настоящее время данные могут вводиться только суперпользователем на админи-
# стративном сайте. Однако разрешать пользователям работу на административном
# сайте явно нежелательно, поэтому мы воспользуемся средствами построения форм
# Django для создания страниц, на которых пользователи смогут вводить данные.

# --------------------------------------------------------------------------------------------------------------------

# Добавление новых тем

# Начнем с возможности создания новых тем. Страницы на базе форм добавляются
# практически так же, как и те страницы, которые мы уже строили ранее: вы опреде-
# ляете URL, пишете функцию представления и создаете шаблон. Принципиальное
# отличие — добавление нового модуля forms.py, содержащего функциональность
# форм.

# Объект ModelForm

# Любая страница, на которой пользователь может вводить и отправлять инфор-
# мацию, является формой, даже если на первый взгляд она на форму не похожа.
# Когда пользователь вводит информацию, необходимо проверить, что он ввел
# корректные данные, а не вредоносный код (например, код для нарушения ра-
# боты сервера). Затем проверенная информация обрабатывается и сохраняется
# в нужном месте базы данных. Django автоматизирует бульшую часть этой
# работы.
# Простейший способ построения форм в Django основан на использовании класса
# ModelForm, который автоматически строит форму на основании моделей, опреде-
# ленных в главе 18. Ваша первая форма будет создана в файле forms.py, который
# должен находиться в одном каталоге с models.py:

# forms.py
#
# from django import forms
# from .models import Topic
#  class TopicForm(forms.ModelForm):
# class Meta:
#  model = Topic
#  fields = ['text']
#  labels = {'text': ''}

# Сначала импортируется модуль forms и модель, с которой мы будем работать:
# Topic. В точке  определяется класс с именем TopicForm, наследующий от forms.
# ModelForm. Простейшая версия ModelForm состоит из вложенного класса Meta,
# который сообщает Django, на какой модели должна базироваться форма и какие
# поля на ней должны находиться. В точке  форма создается на базе модели Topic,
# а на ней размещается только поле text . Код  приказывает Django не генериро-
# вать подпись
# для текстового поля.

# --------------------------------------------------------------------------------------------------------------------

# URL-адрес для new_topic

# URL-адрес новой страницы должен быть простым и содержательным, поэтому
# после того, как пользователь выбрал команду создания новой темы, он направля-
# ется по адресу http://localhost:8000/new_topic/. Ниже приведена схема URL для
# страницы new_topic, которая добавляется в learning_logs/urls.py:

# urls.py
# ...
# urlpatterns = [
# ...
# # Страница для добавления новой темы
# url(r'^new_topic/$', views.new_topic, name='new_topic'),
# ]

# Эта схема URL будет отправлять запросы функции представления new_topic(),
# которую мы сейчас напишем.

# --------------------------------------------------------------------------------------------------------------------

# Функция представления new_topic()

# Функция new_topic() должна обрабатывать две разные ситуации: исходные за-
# просы страницы new_topic (в этом случае должна отображаться пустая форма)
# и обработка данных, отправленных через форму. Затем она должна перенаправить
# пользователя обратно на страницу topics:

# views.py
#
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from .models import Topic
# from .forms import TopicForm
# ...
# def new_topic(request):
# """Определяет новую тему."""
#  if request.method != 'POST':
# # Данные не отправлялись; создается пустая форма.
#  form = TopicForm()
# else:
# # Отправлены данные POST; обработать данные.
#  form = TopicForm(request.POST)
#  if form.is_valid():
#  form.save()
#  return HttpResponseRedirect(reverse('learning_logs:topics'))
#  context = {'form': form}
# return render(request, 'learning_logs/new_topic.html', context)

# Мы импортируем класс HttpResponseRedirect, который будет использоваться
# для перенаправления пользователя к странице topics после отправки введенной
# темы. Функция reverse() определяет URL по заданной схеме URL (то есть Django
# сгенерирует URL при запросе страницы). Также импортируется только что напи-
# санная форма TopicForm.

# --------------------------------------------------------------------------------------------------------------------

# Запросы GET и POST

# При построении веб-приложений используются два основных типа запросов —
# GET и POST. Запросы GET используются для страниц, которые только читают
# данные с сервера, а запросы POST обычно используются в тех случаях, когда
# пользователь должен отправить информацию через форму. Для обработки всех
# наших форм будет использоваться метод POST (существуют и другие разновид-
# ности запросов, но в нашем проекте они не используются).
# Функция new_topic() получает в параметре объект запроса. Когда пользователь
# впервые запрашивает эту страницу, его браузер отправляет запрос GET. Когда
# пользователь уже заполнил и отправил форму, его браузер отправляет запрос
# POST. В зависимости от типа запроса мы определяем, запросил ли пользователь
# пустую форму (запрос GET) или предлагает обработать заполненную форму (за-
# прос POST).
# Метод запроса — GET или POST — проверяется в точке . Если метод запро-
# са отличен от POST, вероятно, используется запрос GET, поэтому необходимо
# вернуть пустую форму (даже если это запрос другого типа, это все равно безопас-
# но). Мы создаем экземпляр TopicForm , сохраняем его в переменной form и от-
# правляем форму шаблону в словаре context . Так как при создании TopicForm
# аргументы не передавались, Django создает пустую форму, которая заполняется
# пользователем.
# Если используется метод запроса POST, выполняется блок else, кото-
# рый обрабатывает
# данные, отправленные в форме. Мы создаем экземпляр
# TopicForm  и передаем ему данные, введенные пользователем, хранящиеся
# в request.POST. Возвращаемый объект form содержит информацию, отправлен-
# ную пользователем.
# Отправленную информацию нельзя сохранять в базе данных до тех пор, пока она
# не будет проверена . Функция is_valid() проверяет, что все обязательные поля
# были заполнены (все поля формы по умолчанию являются обязательными), а вве-
# денные данные соответствуют типам полей — например, что длина текста меньше
# 200 символов, как было указано в файле models.py в главе 18. Автоматическая про-
# верка избавляет нас от большого объема работы. Если все данные действительны,
# можно вызвать метод save() , который записывает данные из формы в базу дан-
# ных. После того как данные будут сохранены, страницу можно покинуть. Мы ис-
# пользуем вызов reverse() для получения URL-адреса страницы topics и передаем
# его функции HttpResponseRedirect() , перенаправляющей браузер пользователя
# на страницу topics. На этой странице пользователь видит только что введенную
# им тему в общем списке тем.

# -------------------------------------------------------------------------------------------------------------------

# Шаблон new_topic  c 412

# Теперь создадим новый шаблон с именем new_topic.html для отображения только
# что созданной формы:

# new_topic.html
#
# {% extends "learning_logs/base.html" %}
# {% block content %}
# <p>Add a new topic:</p>
#  <form action="{% url 'learning_logs:new_topic' %}" method='post'>
#  {% csrf_token %}
#  {{ form.as_p }}
#  <button name="submit">add topic</button>
# </form>
#
# {% endblock content %}

# Этот шаблон расширяет base.html, поэтому он имеет такую же базовую структуру,
# как и остальные страницы Learning Log. В точке  определяется форма HTML.
# Аргумент action сообщает серверу, куда передавать данные, отправленные фор-
# мой; в данном случае данные возвращаются функции представления new_topic().
# Аргумент method приказывает браузеру отправить данные в запросе типа POST.
# Django использует шаблонный тег {% csrf_token %}  для предотвращения по-
# пыток получения несанкционированного доступа к серверу (атаки такого рода
# называются межсайтовой подделкой запросов). В точке  отображается форма;
# это наглядный пример того, насколько легко в Django выполняются такие стан-
# дартные операции, как отображение формы. Чтобы автоматически создать все
# поля, необходимые для отображения формы, достаточно включить шаблонную
# переменную {{ form.as_p }}. Модификатор as_p приказывает Django отобра-
# зить все элементы формы в формате абзацев — это простой способ аккуратного
# отображения
# формы.
# Django не создает кнопку отправки данных для форм, поэтому мы определяем ее
# в точке .

# Создание ссылки на страницу new_topic
# Далее ссылка на страницу new_topic создается на странице topics:

# topics.html
#
# {% extends "learning_logs/base.html" %}
# {% block content %}
# <p>Topics</p>
# <ul>
# ...
# </ul>
# <a href="{% url 'learning_logs:new_topic' %}">Add a new topic:</a>
# {% endblock content %}

# Разместите ссылку после списка существующих тем. Полученная форма изобра-
# жена на рис. 19.1. Воспользуйтесь ею и добавьте несколько своих тем.

# --------------------------------------------------------------------------------------------------------------------

# Добавление новых записей

# Теперь, когда пользователь может добавлять новые темы, он также захочет добав-
# лять новые записи. Мы снова определим URL, напишем новую функцию и шаблон
# и создадим ссылку на страницу. Но сначала нужно добавить в forms.py еще один
# класс.

# Класс EntryForm

# Мы должны создать форму, связанную с моделью Entry, но более специализиро-
# ванную по сравнению с TopicForm:

# forms.py

# from django import forms
#
# from .models import Topic, Entry
#
# class TopicForm(forms.ModelForm):
# ...
#
# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = ['text']
#       labels = {'text': ''}
#       widgets = {'text': forms.Textarea(attrs={'cols': 80})}

# Сначала в команду import к Topic добавляется Entry. Новый класс EntryForm на-
# следует от forms.ModelForm и содержит вложенный класс Meta с указанием модели,
# на которой он базируется, и поле, включаемое в форму. Полю 'text' снова назна-
# чается пустая надпись .
# В точке  включается атрибут widgets. Виджет (widget) представляет собой эле-
# мент формы HTML: однострочное или многострочное текстовое поле, раскрываю-
# щийся список и т. д. Включая атрибут widgets, вы можете переопределить виджеты,
# выбранные Django по умолчанию. Приказывая Django использовать элемент forms.
# Textarea, мы настраиваем виджет ввода для поля 'text', чтобы ширина текстовой
# области составляла 80 столбцов вместо значения по умолчанию 40. У пользователя
# будет достаточно места для создания содержательных записей.

# ---------------------------------------------------------------------------------------------------------------------

