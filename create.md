## To check django version  
* `python -m django --version  `
or  
*` django-admin --version`


## To create a project file of django the command is  
* `django-admin startproject project_name`  
* Let’s look at what startproject created:  
* djangotutorial/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py  
### These files are:
* manage.py: A command-line utility that lets you interact with this Django project in various ways. 
* mysite/: A directory that is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
* mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. 
* mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
* mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. 
* mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. 
* mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.



## To open that file 
* ` cd project_name ` 

## To make new directory
* ` mkdir dir_name `

## To print all dirctories in the project
* `dir`
 
## To start server
* `python manage.py runserver`  
(i.e. `http://127.0.0.1:8000/`)

## To create your app, make sure you’re in the same directory as manage.py and type this command:
*  `python manage.py startapp polls`  # poll is app name
* That’ll create a directory polls, which is laid out like this:
* polls/  

     __init__.py  
    admin.py  
    apps.py  
    migrations/  
     __init__.py  
    models.py  
    tests.py  
    views.py

## To create environment
* `workon test`


##### MVT(Model View Template)
##### DTL(Django Template Language)

## To create a new folder in telusko folder
C:\Users\telusko\projects>workon test      
```
(test) C:\Users\telusko\projects>cd telusko
(test) C:\Users\telusko\projects>python manage.py collectstatic     (it will create a new folder names as "assets" which will copy all the files of "static" folder in telusko folder after writting some code in settings  
```
```py
The code written in settings is: STATICFILES_DIRS = [  
    os.path.join(BASE_DIR, 'static')  
]  
STATIC_ROOT = os.path.join(BASE_DIR, 'assets'))  
```
## To create database  
* To create a database first install a database software (i.e. pgadmin)  
* create a database file there and after that  go to pycharm terminal and "pip install psycopg2"  
* Then after that `pip install pillow` and make a new directory named as migrations ("python manage.py makemigrations")  
  A directory will be created which have a file named as 0001_initial.py (Which is migration number) 
* Then  `python manage.py sqlmigrate` travello 0001 (This will create a table)  
* The `python manage.py migrate` will migrate the created table.  
* Re-migration can be done by using `python manage.py makemigrations` (its helps to detect errors and solve them.)

## To create superuser admin in jango
* In Terminal enter `python manage.py help` and it will give you many options and ask you to select an option.
* You have to select createsuperuser option as `python manage.py createsuperuser`. And it will ask you for further details and then create superuser admin.
* After that you can access your website as admin by searching `localhost:8000/admin/` or `http://127.0.0.1:8000/admin` and filling superuser name and password.

## URL
* If you create a new app you have to connect the app URL with the original URL.

## get_absolute_url()
* The get_absolute_url function in your Django model is used to provide a canonical URL for an object. When you define this method in a model, Django knows what URL to redirect to after an instance of this model is created or updated.
``` py 
from django.db import models
from django.urls import reverse


class PrintEaseSignModel(models.Model):
    username = models.CharField(max_length=100),
    email = models.EmailField(max_length=254),
    password = models.CharField(max_length=200),

    def get_absolute_url(self):
        return reverse("index")
```
