## Authentication in Django:
* Give app name in `settings.py` of main file's "INSTALLED_APPS" section.
* after that create a list beneath "INSTALLED_APPS" as:
```py
AUTHENTICATION_BACKENDS = [
    'django.conterib.auth.backends.ModelBackend'
] 
```
This will helps us to use Authentication backup in our app.
* Now in "auth_app" in "views.py" create viewqs as "register_view", "login_view", "dashboard_view", "logout_view" for register, login, dashboard, logout respectively.
* The "UserCreationForm" in "def register_view(request):" is inbuilt and imported from django as "from django.contrib.auth.forms import UserCreationForm".
* "from django.contrib.auth import login, logut" is used for login and logout.
* In the "app.html" code is taken from w3school (the CDN of code).
* In body tag the "{% block content %}" is created and end as {% endblock %}, in this "block content" all the contents will be. 
* And after that in "register.html" file the "{% extends 'app.html' %}" is extended. and
```py
{% block content %}

{% endblock %}
```
is created and in this block the forms can be creted using html coding.
* The {% csrf_token %} is created and the {{form.as_p}} is used to create form automatically (but the interface will not be so good, so we have to create registration form interface by ourself.)
* Now we have to create "urls" for the form. In "urls.py" the link or url of functions created in "views.py" is given in urlpattern=[].
* Now we have to inform main "urls.py" file that we also have an another "urls.py" file in "auth_app" app, by including "auth_app.urls" as:
``` py
urlpatterns = [
    path('auth/', include('auth_app.urls')
]
```
* Now we will run the server executing "pyhton manage.py runserver" command in Terminal.
* The user name in registration form will be given in jija format as "{{form.username.id_for_label}}"  
``` 
    <label for= "{{form.username.id_for_label}}">Username</label>
    <input type = "text" name="{{ form.username.name }}" class="form-control" value="{{form.username.value}}" />
    <span class = "text-danger">{{form.username.errors}}</spna>
```    
and after that we will create two lables for password1 and a another label for password2 and crreate a button "Submit".
* After that we will write "initial_data = {'username':'', 'password1':'', 'password2':''}" in else part of "register" function.
* And we also have to define it's variable which is "initial_data" in "UserCreationForm()" as UserCreationForm(initial = initial_data0)
* In "logout()" function the user send a request and redirect to login page.
* In login() function on views.py the "AuthenticationForm()" function will be used instead of "UserCreationForm".
* The new form for "login.html" will be created, and in it we will create a login form.
* In "login.html" the button of "create a new account" will be creted, which will take us to register page.
* And in "register.html" the "login" button will be created which will takeus to login page.
* For "dashboard" we will create a 'dashboard.html' file in which the data of login and logout user will be shown and "app.html" should be extended in this file.
* The logout button link is also made here.
* The following code will show that the password enter in login form is wrong(if the login password is wrong)
```
{% if form.non_feild_errors %}
<small class="text-danger">
   {{ form.non_feild_errors.as_url }}
{% endif %}
```
It should be in "login.html" file.















