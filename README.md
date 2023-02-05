# Blog pet projects
## (Flask project)
### Сайт развёрнут на платформе Pythonanywhere http://aleshichev.pythonanywhere.com/
##### Сайт был развёрнут на платформе Heroku https://my-flask-projects-blog.herokuapp.com/
Блог личных проектов, который имеет форму регистрации и работает в режимах:
- **администратор** (может просматривать, создавать, редактировать, удалять статьи)
- **зарегистрированный пользователь** (может просматривать статьи и писать комментарии к ним)
- **обычный пользователь** (может только просматривать статьи).

На странице **main page (home)** отображается список проектов. На странице **register** расположена форма регистрации. На странице **login**– форма аутентификации. На странице **about** – описание об авторе сайта. На странице **contact** расположена форма отправки **email** на мою почту. Каждая статья отображается на отдельной странице и имеет **форму для записи комментариев**, которые отображаются под этой формой. В **“футере”** находятся ссылки на мой linkedin и githab. 
К сайту подключена **SQLite** база данных.

## Используемые ресурсы
-	Шаблон **Bootstrap**
-	**Sqlite**
-	**Flask** 
## Модули и библиотеки:
**smtplib, os, date, flask_login, SQLAlchemy, CKEditor, WTForms, request, wraps, flask_gravatar, flask_bootstrap, werkzeug.security**
 
## Структура проекта
На основе **Фреймворка Flask** и шаблона **Bootstrap** создана модель отображения структуры проекта:
1.	Папка **static** - содержит стили **Css, Js и картинки** отображаемые на страницах сайта
2.	Папка **templates** - содержит шаблоны **HTML** страниц сайта
3.	Файл **main.py** – содержит основной код программы. (Описание ниже)
4.	Файл **forms.py** – содержит  4 класса, на основе которых создано 4 формы для заполнения данных **PostForm, RegisterForm, LoginForm, CommentForm**.
5.	Файл **posts.db** – **Sqlite** база данных, которая содержит 3 таблицы данных: **User, BlogPost, Comment**.
6.	Файл **Procfile** – содержит сообщение для запуска процессов на **Heroku**
7.	Файл **requirements.txt** – имеет список используемых версий модулей и библиотек в проекте.

## Main.py 
Вначале файл находится блок импорта необходимых модулей, библиотек и пакетов, используемых в проекте.  Затем - блок констант данных, которые используются в функции **def send_emails()** для отправки почты. Далее – блок создания **приложения Flask** и подключения всех дополнительных компонентов в приложение **CKEditor, Bootstrap, Gravatar, SQLAlchemy, LoginManager**. Затем представлена функция **def load_user()**, которая идентифицирует зарегистрированного пользователя. Далее идут 3 класса **User, BlogPost, Comment**, которые создают 3 соответствующие таблицы в базе данных (файл **posts.db** ). Затем представлена функция-декоратор **def admin_only()**, которая определяет администратора. За ней – функция **def send_email**, которая отвечает за отправку сообщения на почту администратора. 
#### Затем идёт основная логика функционирование и отображения страниц сайта:
- **def home()** - главная страница. Отображает список всех статей. Возвращает шаблон **index.html**
- **def register()** - страница регистрации. Отображает форму регистрации шаблон **register.html**. Если форма заполнена правильно перенаправляет пользователя на домашнюю страницу. 
- **def login()** - страница аутентификации. Отображает форму аутентификации шаблон **login.html**. Проверяет ошибки заполнения формы. Если форма заполнена правильно перенаправляет пользователя на домашнюю страницу. 
- **def post()** - страница отображения отдельного поста и блока комментариев. Проверяет аутентификацию пользователя (если пользователь не зарегистрирован перенаправляет на страницу **login**). Возвращает шаблон **post.html**.
- **def add_new_post()** -  страница содержит форму заполнения информации для нового поста. Отображает шаблон **make-post.html**. Если пост создан, перенаправляет на страницу **home**. Только для администратора **@admin_only**.
- **def edit_post()** - страница отображает форму редактирования информации для нового поста. Отображает шаблон **make-post.html**. Если пост отредактирован, перенаправляет на страницу **post**. Только для администратора **@admin_only**.
- **def about()** - отображает информацию о администраторе сайта, возвращает шаблон страницы **about.html**.
- **def contact()** - на странице расположена форма отправки email администратора сайта. Возвращает страницу **contact.html**.
- **def delete-post()** - функция удаления постов. Перенаправляет пользователя на страницу **home**. Только для администратора **@admin_only**.
- **def logout()** - функция отвечает за выход пользователя из аутентификации. Перенаправляет пользователя на страницу **home**.




