# Blog flask
## (Flask project)
### The site is deployed on the platform Pythonanywhere http://aleshichev.pythonanywhere.com/
##### The site was deployed on the platform Heroku https://my-flask-projects-blog.herokuapp.com/
Blog of personal projects, which has a registration form and works in modes:
- **administrator** (can view, create, edit, delete articles)
- **registered user** (can view articles and write comments on them)
- **regular user** (can only view articles).

On the **main** page project list is displayed. On the page **register** you will find the registration form. On the **login** page is the authentication form. In the **about** page is a description about the author of the site. On the **contact** page there is a form to send **email** to my inbox.  Each article is displayed on a separate page and has a **form for writing comments**, which are displayed below that form. In the **footer** are links to my linkedin and githab. 
The site is connected to a **SQLite** database.

## Resources:
- Template **Bootstrap**
- **Sqlite**
- **Flask** 
## Modules and libraries:
**smtplib, os, date, flask_login, SQLAlchemy, CKEditor, WTForms, request, wraps, flask_gravatar, flask_bootstrap, werkzeug.security**
 
## Project Structure
Based on the **Flask** framework and the **Bootstrap** template, a project structure mapping model has been created:
1.	Folder **static** - contains styles **Css, Js and images** displayed on the pages of the site
2.	Folder **templates** - contains **HTML** templates of the site pages
3.	File **main.py** - contains the main code of the programme. (Description below)
4.	File **forms.py** - contains 4 classes, on the basis of which 4 forms for data filling **PostForm, RegisterForm, LoginForm, CommentForm** are created.
5.	File **posts.db** - **Sqlite** database which contains 3 data tables: **User, BlogPost, Comment**.
6.	The **Procfile** file - contains the message to run processes on **Heroku**
7.	File **requirements.txt** - has a list of used versions of modules and libraries in the project.

## Main.py 
At the beginning of the file is a block of importing necessary modules, libraries and packages used in the project.  Then - a block of data constants that are used in the **def send_emails()** function to send mail. Next is the block of creating a **Flask** application and connecting all the additional components in the application **CKEditor, Bootstrap, Gravatar, SQLAlchemy, LoginManager**. Then the **def load_user()** function is presented, which identifies the logged in user. Next come 3 classes **User, BlogPost, Comment** which create 3 corresponding tables in the database (file **posts.db** ). Then the **def admin_only()** decorator function **def admin_only()** is presented, which defines the administrator. It is followed by the **def send_email** function, which is responsible for sending a message to the administrator's mail. 
#### Then comes the main logic of functioning and displaying the pages of the site:
- **def home()** - home page. Displays a list of all articles. Returns **index.html** template
- **def register()** - registration page. Displays the registration form template **register.html**. If the form is filled out correctly redirects the user to the home page. 
- **def login()** - authentication page. Displays the authentication form template **login.html**. Checks for errors in filling out the form. If the form is filled out correctly redirects the user to the home page. 
- **def post()** - page for displaying individual post and comment block. Checks user authentication (if user is not logged in redirects to **login** page). Returns the **post.html** template.
- **def add_new_post()** - the page contains a form for filling in information for a new post. Displays the **make-post.html** template. If a post is created, redirects to the **home** page. For admin **@admin_only** only.
- **def edit_post()** - page displays a form for editing information for a new post. Displays the **make-post.html** template. If the post is edited, redirects to the **post** page. For admin **@admin_only** only.
- **def about()** - displays information about the site administrator, returns the **about.html** page template.
- **def contact()** - the page contains a form for sending the site administrator's email. Returns the **contact.html** page.only**.
- **def logout()** - the function is responsible for user logout from authentication. Redirects the user to the **home** page.
