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

# URL-адрес для new_entry

# Необходимо включить аргумент topic_id в URL-адрес для создания новой записи,
# потому что запись должна ассоциироваться с конкретной темой. Вот как выглядит
# URL, который мы добавляем в learning_logs/urls.py:
#
# urls.py
# ...
# urlpatterns = [
# ...
# # Страница для добавления новой записи
# path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry')
# ]

# Эта схема URL соответствует любому URL-адресу в форме http://
# localhost:8000/new_entry/id/, где id — число, равное идентификатору темы.
# Выражение (?P<topic_id>\d+) захватывает числовое значение и сохраняет
# его в переменной topic_id. При запросе URL-адреса, соответствующего этой
# схеме, Django передает запрос и идентификатор темы функции представления
# new_entry().

# --------------------------------------------------------------------------------------------------------------------

# Функция представления new_entry()

# Функция представления new_entry очень похожа на функцию добавления новой
# темы:

# views.py
#
# from django.shortcuts import render
# ...
# from .models import Topic
# from .forms import TopicForm, EntryForm
# ...
#
# def new_entry(request, topic_id):
# """Добавляет новую запись по конкретной теме."""
#  topic = Topic.objects.get(id=topic_id)
#  if request.method != 'POST':
# # Данные не отправлялись; создается пустая форма.
#  form = EntryForm()
# else:
# # Отправлены данные POST; обработать данные.
#  form = EntryForm(data=request.POST)
# if form.is_valid():
#  new_entry = form.save(commit=False)
#  new_entry.topic = topic
# new_entry.save()
#  return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
#
# context = {'topic': topic, 'form': form}
# return render(request, 'learning_logs/new_entry.html', context)

# Мы обновляем команду import и включаем в нее только что созданный класс
# EntryForm. Определение new_entry() содержит параметр topic_id для сохранения
# полученного значения из URL. Идентификатор темы понадобится для отображе-
# ния страницы и обработки данных формы, поэтому мы используем topic_id для
# получения правильного объекта темы .
# В точке  проверяется метод запроса: POST или GET. Блок if выполняется для
# запроса GET, и мы создаем пустой экземпляр EntryForm . Для метода запроса
# POST мы обрабатываем данные, создавая экземпляр EntryForm, заполненный
# данными POST из объекта запроса . Затем проверяется корректность данных
# формы. Если данные корректны, необходимо задать атрибут topic объекта записи
# перед сохранением его в базе данных.
# При вызове save() мы включаем аргумент commit=False  для того, чтобы создать
# новый объект записи и сохранить его в new_entry, не сохраняя пока в базе данных.
# Мы присваиваем атрибуту topic объекта new_entry тему, прочитанную из базы дан-
# ных в начале функции , после чего вызываем save() без аргументов. В результате
# запись сохраняется в базе данных с правильной ассоциированной темой.
# В точке  пользователь перенаправляется на страницу темы. При вызове
# reverse() должны передаваться два аргумента: имя схемы URL, для которой
# генерируется URL-адрес, и список аргументов со всеми аргументами, которые
# должны быть включены в URL. Список аргументов содержит всего один элемент
# topic_id. Вызов HttpResponseRedirect() перенаправляет пользователя на стра-
# ницу темы, для которой была создана запись, и пользователь видит новую запись
# в списке записей.

# ---------------------------------------------------------------------------------------------------------------------

# Шаблон new_entry

# new_entry.html
#
# {% extends "learning_logs/base.html" %}
# {% block content %}
#  <p><a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a></p>
# <p>Add a new entry:</p>
#  <form action="{% url 'learning_logs:new_entry' topic.id %}" method='post'>
# {% csrf_token %}
# {{ form.as_p }}
# <button name='submit'>add entry</button>
# </form>
# {% endblock content %}

# В начале страницы выводится тема , чтобы пользователь мог видеть, в какую тему
# добавляется новая запись. Тема также служат ссылкой для возврата к основной
# странице этой темы.
# Аргумент action формы включает значение topic_id из URL, чтобы функция
# представления
# могла связать новую запись с правильной темой . В остальном
# этот шаблон почти не отличается от new_topic.html.

# --------------------------------------------------------------------------------------------------------------------

# Создание ссылки на страницу new_entry  стр 416

# Затем необходимо создать ссылку на страницу new_entry на каждой странице темы:

# topic.html
#
# {% extends "learning_logs/base.html" %}
# {% block content %}
# <p>Topic: {{ topic }}</p>
# <p>Entries:</p>
# <p>
# <a href="{% url 'learning_logs:new_entry' topic.id %}">add new entry</a>
# </p>
# <ul>
# ...
# </ul>
# {% endblock content %}

# Ссылка добавляется перед выводом записей, потому что добавление новой запи-
# си является самым частым действием на этой странице. На рис. 19.2 изображена
# страница new_entry. Теперь пользователь может добавить сколько угодно новых
# тем и новых записей по каждой теме. Опробуйте страницу new_entry, добавив не-
# сколько записей для каждой из созданных вами тем.

# -------------------------------------------------------------------------------------------------------------------

# Добавление записей

# теперь мы создадим страницу, на которой пользователи смогут редактировать
# ранее добавленные записи.
# URL-адрес для edit_entry
# В URL-адресе страницы должен передаваться идентификатор редактируемой
# записи.
# В файл learning_logs/urls.py для этого вносятся следующие изменения:

# urls.py

# ...
# urlpatterns = [
# ...
# # Страница для редактирования записи
# url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
# name='edit_entry'),
# ]

# Идентификатор, переданный в URL (например, http://localhost:8000/edit_entry/1/),
# сохраняется в параметре entry_id. Схема The URL отправляет запросы, соответ-
# ствующие этому формату, функции представления edit_entry().

# ---------------------------------------------------------------------------------------------------------------------

# Функция представления edit_entry()

# Когда страница edit_entry получает запрос GET, edit_entry() возвращает форму
# для редактирования записи. При получении запроса POST с отредактированной
# записью страница сохраняет измененный текст в базе данных:

# views.py
#
# from django.shortcuts import render
# ...
# from .models import Topic, Entry
# from .forms import TopicForm, EntryForm
# ...
# def edit_entry(request, entry_id):
# """Редактирует существующую запись."""
#  entry = Entry.objects.get(id=entry_id)
# topic = entry.topic
# if request.method != 'POST':
# # Исходный запрос; форма заполняется данными текущей записи.
#  form = EntryForm(instance=entry)
# else:
# # Отправка данных POST; обработать данные.
#  form = EntryForm(instance=entry, data=request.POST)
# if form.is_valid():
#  form.save()
#  return HttpResponseRedirect(reverse('learning_logs:topic',
# args=[topic.id]))
# context = {'entry': entry, 'topic': topic, 'form': form}
# return render(request, 'learning_logs/edit_entry.html', context)

# Сначала необходимо импортировать модель Entry. В точке  мы получаем объект
# записи, который пользователь хочет изменить, и тему, связанную с этой записью.
# В блоке if, который выполняется для запроса GET, создается экземпляр EntryForm
# с аргументом instance=entry . Этот аргумент приказывает Django создать форму,
# заранее заполненную информацией из существующего объекта записи. Пользова-
# тель видит свои существующие данные и может отредактировать их.
# При обработке запроса POST передаются аргументы i n s t a n c e = e n t r y
# и data=request.POST , чтобы приказать Django создать экземпляр формы на
# основании информации существующего объекта записи, обновленный данными
# из request.POST. Затем проверяется корректность данных формы. Если данные
# корректны, следует вызов save() без аргументов . Далее происходит перена-
# правление на страницу темы , и пользователь видит обновленную версию от-
# редактированной им записи.

# -------------------------------------------------------------------------------------------------------------------

# Шаблон edit_entry

# Шаблон edit_entry.html очень похож на new_entry.html:

# edit_entry.html
#
# {% extends "learning_logs/base.html" %}
# {% block content %}

# <p><a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a></p>
# <p>Edit entry:</p>
# ❶ <form action="{% url 'learning_logs:edit_entry' entry.id %}" method='post'>
# {% csrf_token %}
# {{ form.as_p }}
# ❷ <button name="submit">save changes</button>
# </form>
# {% endblock content %}

# В точке  аргумент action отправляет форму функции edit_entry() для обработки. Идентификатор записи включается
# как аргумент в тег {% url %} , чтобы функция представления могла изменить правильный объект записи. Кнопка отправки
# данных создается с текстом, который напоминает пользователю, что он сохраняет изменения, а не создает новую запись .

# --------------------------------------------------------------------------------------------------------------------,

# Создание ссылки на страницу edit_entry

# Теперь необходимо включить ссылку на страницу edit_entry в каждую тему на странице со списком тем:

# topic.html
#
# ...
# {% for entry in entries %}
# <li>
# <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
# <p>{{ entry.text|linebreaks }}</p>
# <p>
# <a href="{% url 'learning_logs:edit_entry' entry.id %}">Edit entry</a>
# </p>
# </li>
# ...

# После даты и текста каждой записи включается ссылка редактирования. Мы используем шаблонный тег {% url %} для
# определения схемы URL из именованной схемы edit_entry и идентификатора текущей записи в цикле (entry.id).
# Текст ссылки "edit entry" выводится после каждой записи на странице. На рис. 19.3 показано, как выглядит
# страница со списком тем с этими ссылками.
# Приложение Learning Log уже сейчас содержит большую часть необходимой функциональности. Пользователи могут
# добавлять темы и записи, а также читать любые записи по своему усмотрению. В этом разделе мы реализуем систему
# регистрации пользователей, чтобы любой желающий мог создать свою учетную запись в Learning Log и ввести собственный
# набор тем и записей.

# --------------------------------------------------------------------------------------------------------------------

# Создание учетных записей пользователей

# В этом разделе мы создадим систему регистрации и авторизации пользователей, чтобы люди могли создать учетную запись,
# начать и завершать сеанс работы с приложением. Для всей функциональности, относящейся к работе с пользователями, будет
# создано отдельное приложение. Мы также слегка изменим модель Topic, чтобы каждая тема была связана с конкретным
# пользователем.

# ------------------------------------------------------------------------------------------------------------------

# Приложение users

# Начнем с создания нового приложения users командой startapp:
#
# (ll_env)learning_log$ python manage.py startapp users
# (ll_env)learning_log$ ls
# ❶ db.sqlite3 learning_log learning_logs ll_env manage.py users
# (ll_env)learning_log$ ls users
# ❷ __init__.py admin.py apps.py migrations models.py tests.py views.py
#
# Эта команда создает новый каталог с именем users , структура которого повторяет структуру каталогов приложения
# learning_logs .
# Добавление пользователей в settings.py
# Новое приложение необходимо добавить в settings.py:

# settings.py

# ...
# INSTALLED_APPS = [
# # Мои приложения
# 'learning_logs',
# 'users',
# # Приложения django по умолчанию.
# ...
# ]
# ...

# Django включает приложение users в общий проект.

# ---------------------------------------------------------------------------------------------------------------------

# Включение URL-адресов из users

# Затем необходимо изменить корневой файл urls.py, чтобы он включал URL-адреса,
# написанные для приложения users:

# urls.py
#
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
# path('admin/', admin.site.urls),
# path('users/', include('users.urls')),
# path('', include('learning_logs.urls')),
# ]

# Добавим строку для включения файла urls.py из users. Эта строка будет соответствовать любому URL-адресу, начинающемуся
# со слова users, например http://localhost:8000/users/login/.

# --------------------------------------------------------------------------------------------------------------------

# Страница входа

# Начнем с реализации страницы входа. Мы воспользуемся стандартным представлением login, которое предоставляет
# Django, так что шаблон URL выглядит немного иначе. Создайте новый файл urls.py в каталоге learning_log/users/
# и добавьте в него следующий код:

# urls.py
#
# """Определяет схемы URL для пользователей"""
# from django.urls import path, include
#
# ❶ app_name = 'users'
# urlpatterns = [
# # Включить URL авторизации по умолчанию.
# ❷ path('', include('django.contrib.auth.urls')),
# ]

# Сначала импортируется функция path, а затем функция include для включения аутентификационных URL-адресов по умолчанию,
# определенных Django. Эти URL-адреса по умолчанию включают именованные схемы, такие как 'login' и 'logout'. Переменной
# app_name присваивается значение 'users', чтобы инфраструктура Django могла отличить эти URL-адреса от URL-адресов,
# принадлежащих другим приложениям . Даже URL-адреса по умолчанию, предоставляемые Djano, при включении в файл urls.py
# приложения users будут доступны через пространство имен users.

# Схема страницы входа соответствует URL http://localhost:8000/users/login/ . Когда Django читает этот URL-адрес, слово
# users указывает, что следует обратиться к users/urls.py, а login сообщает о том, что запросы должны отправляться
# представлению login по умолчанию.

# --------------------------------------------------------------------------------------------------------------------

# Шаблон login

# Когда пользователь запрашивает страницу входа, Django использует свое представление login по умолчанию,
# но мы все равно должны предоставить шаблон для этой страницы. Аутентификационные представления по умолчанию
# ищут шаблоны в каталоге с именем registration, поэтому вы должны создать этот каталог. В каталоге
# learning_log/users/ создайте каталог с именем templates, а внутри него — еще один каталог с именем registration.
# Вот как выглядит шаблон login.html, который должен находиться в learning_log/users/templates/registration/:

# login.html
#
# {% extends "learning_logs/base.html" %}
# {% block content %}
# ❶ {% if form.errors %}
# <p>Your username and password didn't match. Please try again.</p>
# {% endif %}
# ❷ <form method="post" action="{% url 'users:login' %}">
# {% csrf_token %}
# ❸ {{ form.as_p }}
# ❹ <button name="submit">log in</button>
# ❺ <input type="hidden" name="next"
# value="{% url 'learning_logs:index' %}" />
# </form>
# {% endblock content %}

# Шаблон расширяет base.html, чтобы страница входа по оформлению и поведению была похожа на другие страницы сайта.
# Обратите внимание: шаблон в одном приложении может расширять шаблон из другого приложения.
# Если у формы установлен атрибут errors, выводится сообщение об ошибке . В нем говорится,
# что комбинация имени пользователя и пароля не соответствует информации, хранящейся в базе данных.
# Мы хотим, чтобы представление обработало форму, поэтому аргументу action присваивается URL страницы
# входа . Представление отправляет форму шаблону, мы должны вывести форму  и добавить кнопку отправки
# данных . В точке  включается скрытый элемент формы 'next'; аргумент value сообщает Django, куда
# перенаправить пользователя после успешно выполненного входа. В нашем случае пользователь возвращается
# обратно на домашнюю страницу.

# -------------------------------------------------------------------------------------------------------------------

# Создание ссылки на страницу входа

# Добавим ссылку на страницу входа в base.html, чтобы она присутствовала на каждой странице. Ссылка не должна
# отображаться, если пользователь уже прошел процедуру входа, поэтому она вкладывается в тег {% if %}:

# base.html
#
# <p>
# <a href="{% url 'learning_logs:index' %}">Learning Log</a> -
# <a href="{% url 'learning_logs:topics' %}">Topics</a> -
# ❶ {% if user.is_authenticated %}
# ❷ Hello, {{ user.username }}.
# {% else %}
# ❸ <a href="{% url 'users:login' %}">log in</a>
# {% endif %}
# </p>
# {% block content %}{% endblock content %}

# В системе аутентификации Django в каждом шаблоне доступна переменная user, которая всегда имеет атрибут
# is_authenticated: атрибут равен True, если пользо
# ватель прошел проверку, и False в противном случае. Это позволяет вам выводить разные сообщения для проверенных
# и непроверенных пользователей.
# В данном случае мы выводим приветствие для пользователей, выполнивших вход . У проверенных пользователей
# устанавливается дополнительный атрибут username, который обеспечит личную настройку приветствия и напомнит
# пользователю о том, что вход был выполнен . В точке  выводится ссылка на страницу входа для пользователей,
# которые еще не прошли проверку.

# -------------------------------------------------------------------------------------------------------------------

# Использование страницы входа

# Учетная запись пользователя уже создана; попробуем ввести данные и посмотрим, работает ли страница.
# Откройте страницу http://localhost:8000/admin/. Если вы все еще работаете с правами администратора,
# найдите ссылку выхода в заголовке и щелкните на ней.
# После выхода перейдите по адресу http://localhost:8000/users/login/. На экране должна появиться страница
# входа, похожая на рис. 19.4. Введите имя пользователя и пароль, заданные ранее, и вы снова должны
# оказаться на странице со списком. В заголовке страницы должно выводиться сообщение с указанием имени пользователя.

# -------------------------------------------------------------------------------------------------------------------

# Выход

# Теперь необходимо предоставить пользователям возможность выхода из приложения. Мы включим в base.html ссылку
# для выхода пользователя; при щелчке на этой ссылке открывается страница, подтверждающая, что выход был выполнен
# успешно.

# -------------------------------------------------------------------------------------------------------------------

# Добавление ссылки для выхода

# Теперь нужно создать ссылку для выхода. Мы добавим ее в файл base.html, чтобы она была доступна
# на каждой странице, и включим в секцию {% if user.is_authenticated %}, чтобы ссылка была видна только
# пользователям, уже выполнившим вход:

# base.html
#
# ...
# {% if user.is_authenticated %}
# Hello, {{ user.username }}.
# <a href="{% url 'users:logout' %}">log out</a>
# {% else %}
# ...
# По умолчанию схеме URL для выхода назначается имя 'logout'.

# -------------------------------------------------------------------------------------------------------------------

# Страница подтверждения выхода

# Пользователь должен знать, что выход прошел успешно, поэтому представление по умолчанию для выхода строит
# страницу на базе шаблона logged_out.html, который мы сейчас создадим. Он представляет простую страницу с
# уведомлением о том, что пользователь вышел из сеанса работы с приложением. Сохраните файл в каталоге
# templates/registration — в том же каталоге, в котором был сохранен файл login.html:

# logged_out.html
#
# {% extends "learning_logs/base.html" %}
# {% block content %}
# <p>You have been logged out. Thank you for visiting!</p>
# {% endblock content %}

# Ничего другого на этой странице быть не должно, потому что base.html предоставляет ссылки на домашнюю страницу
# и страницу входа на случай, если пользователь захочет вернуться к какой-либо из этих страниц.
# На рис. 19.5 изображена страница выхода так, как ее видит пользователь, выполнивший вход. Оформление страницы
# минимально, потому что сейчас нас в первую очередь интересует работа сайта. Когда необходимые функции заработают,
# можно переходить к стилевому оформлению сайта и приданию ему более профессионального вида.

# -------------------------------------------------------------------------------------------------------------------

# Страница регистрации

# Теперь мы построим страницу для регистрации новых пользователей. Для этой цели мы используем класс
# Django UserCreationForm, но напишем собственную функцию представления и шаблон.

# URL-адрес регистрации

# Следующий код предоставляет шаблон URL для страницы регистрации — также в файле users/urls.py:
#
# urls.py
#
# """ Определяет схемы URL для пользователей. """
# from django.urls import path, include
# from . import views
# app_name = 'users'
# urlpatterns = [
# # Включить URL авторизации по умолчанию.
# path('', include('django.contrib.auth.urls')),
# # Страница регистрации.
# path('register/', views.register, name='register'),
# ]

# Мы импортируем модуль views из users; этот модуль необходим, потому что мы пишем собственное представление
# для страницы регрессии. Шаблон соответствует URL http://localhost:8000/users/register/ и отправляет запросы
# функции register(), которую мы сейчас напишем.

# -------------------------------------------------------------------------------------------------------------------

# Функция представления register()

# Функция представления register() должна вывести пустую форму регистрации при первом запросе страницы регистрации,
# а затем обработать заполненную форму регистрации при отправке данных. Если регистрация прошла успешно, функция
# также должна выполнить вход для нового пользователя. Включите следующий код в users/views.py:

# views.py
#
# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
#
# def register(request):
# """Регистрирует нового пользователя."""
# if request.method != 'POST':
# # Выводит пустую форму регистрации.
# ❶ form = UserCreationForm()
# else:
# # Обработка заполненной формы.
# ❷ form = UserCreationForm(data=request.POST)
# ❸ if form.is_valid():
# ❹ new_user = form.save()
# # Выполнение входа и перенаправление на домашнюю страницу.
# ❺ login(request, new_user)
# ❻ return redirect('learning_logs:index')
# # Вывести пустую или недействительную форму.
# context = {'form': form}
# return render(request, 'users/register.html', context)

# Сначала импортируются функции render() и redirect(). Затем мы импортируем функцию login() для выполнения входа
# пользователя, если регистрационная информация верна. Также импортируется класс UserCreationForm по умолчанию.
# В функции register() мы проверяем, отвечает ли функция на запрос POST. Если нет, создается экземпляр UserCreationForm,
# не содержащий исходных данных .
# В случае ответа на запрос POST создается экземпляр UserCreationForm, основанный на отправленных данных .
# Мы проверяем,что данные верны ; в данном случае что имя пользователя содержит правильные символы, пароли совпадают,
# а пользователь не пытается вставить вредоносные конструкции в отправленные данные.
# Если отправленные данные верны, мы вызываем метод save() формы для сохранения имени пользователя и хеша пароля
# в базе данных . Метод save() возвращает только что созданный объект пользователя, который сохраняется в new_user.
# После того как информация пользователя будет сохранена, мы выполняем вход; этот процесс состоит из двух шагов:
# сначала вызывается функция login() с объектами request и new_user , которая создает действительный сеанс для
# нового пользователя. Наконец, пользователь перенаправляется на домашнюю страницу , где приветствие в заголовке
# сообщает о том, что регистрация прошла успешно.
# В конце функции строится страница, которая будет либо пустой формой, либо отправленной формой, содержащей
# недействительные данные.

# -------------------------------------------------------------------------------------------------------------------

# Шаблон регистрации

# Шаблон страницы регистрации похож на шаблон страницы входа. Проследите за тем, чтобы он был сохранен в одном
# каталоге с login.html:

# register.html
#
# {% extends "learning_logs/base.html" %}
# {% block content %}
# <form method="post" action="{% url 'users:register' %}">
# {% csrf_token %}
# {{ form.as_p }}
# <button name="submit">register</button>
# <input type="hidden" name="next" value="{% url 'learning_logs:index' %}" />
# </form>
# {% endblock content %}

# Мы снова используем метод as_p, чтобы инфраструктура Django могла правильно отобразить все поля формы, включая
# все сообщения об ошибках, если форма была заполнена неправильно.

# -------------------------------------------------------------------------------------------------------------------

# Создание ссылки на страницу регистрации

# Следующий шаг — добавление кода для вывода ссылки на страницу регистрации для любого пользователя, еще
# не выполнившего вход:

# base.html
#
# ...
# {% if user.is_authenticated %}
# Hello, {{ user.username }}.
# <a href="{% url 'users:logout' %}">log out</a>
# {% else %}
# <a href="{% url 'users:register' %}">Register</a> -
# <a href="{% url 'users:login' %}">log in</a>
# {% endif %}
# ...

# Теперь пользователи, выполнившие вход, получат персональное приветствие и ссылку для выхода. Другие
# пользователи видят ссылку на страницу регистрации и ссылку для входа. Проверьте страницу регистрации,
# создав несколько учетных записей с разными именами пользователей.
# В следующем разделе доступ к некоторым страницам будет ограничен, чтобы страницы были доступны только
# для зарегистрированных пользователей. Также необходимо позаботиться о том, чтобы каждая тема принадлежала
# конкретному пользователю.

# ПРИМЕЧАНИЕ Такая система регистрации позволяет любому пользователю создать сколько угодно учетных
# записей Learning Log. Однако некоторые системы требуют, чтобы пользователь подтвердил свою заявку,
# отправляя сообщение электронной почты, на которое пользователь должен ответить. При таком подходе в
# системе будет создано меньше спамерских учетных записей, чем в простейшей системе из нашего примера.
# Но пока вы только учитесь строить приложения, вполне нормально тренироваться на упрощенной системе
# регистрации вроде используемой нами.

# -------------------------------------------------------------------------------------------------------------------
