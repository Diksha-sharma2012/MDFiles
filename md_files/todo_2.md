## The "blueaves" project file is created by running command:   
 `django-admin startproject project_name`

## Then I create new app by runnnig following command
`python manage.py stratapp todo_2`  

* The manage.py file in the created project helps to crete all Apps in the project.
* So after that in the "blueaves" project's "settings" file, I give the name of my app "todo_2" in "INSTALLED_APPS" block as 'todo_2'  
* In the views.py file of app we will add things that we want to add in the view.  
* In the models.py app we create tables.
## Models.py  
* In models.py file I create a class as:  
````py 
class TodoModel(models.Model):         #we write models.Model because its a model
        title = models.CharField(max_length=1000)
        description = models.TextField()
        completed = models.BooleanField(default=False)

        def __str__(self):               
            return self.title       ##This function show that when we call 'Todo' class it will return title as string.(It is optional and i did not add it in my code.)    
````  
* When we created our table in models.py, then we have to inform to django that we created the table in models.py by make migrations as:  
`python manage.py makemigrations`  and a new fike named as '0001_initial.py' is created in migrations.py.  
* Then we have to to migrate it as:  `python manage.py migrate`     (Now our tables are ready in models.py, and we have to ready our view in views.py).  

## views.py  
* In  `views.py ` we have to load list view as:  
```` py

def todo_list(request):
    return render(request, 'todo2/todo_2.html')     #render is used to render the template, request is used to pass the request and the path of html file is given as 'todo/todo_2.html'
````
## I created a templates folder where all the html files of apps are stored.  
* I store 'todo_2.html' file in a folder named "todo2" in templates folder.  

## Give app's link to urls of main project and create path to run  
* In the 'urls.py' file of main project (i.e. blueaves), I add the app name as:  
``` py
 path('todo2/', include('todo_2.urls'))   #in the urlpatterns block
 ```
## After that in the app directory I create a file named as "urls.py", In which I import the todo views.py and give path of the function of views.py  
```` py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo_list)
]
````
## And after that I run the server as: `` python manage.py runserver `` to check that if the server is running or not. 

## settings.py (blueaves)  
* In 'blueaves/settings.py', I give the templates link (behind 'BASE_DIR' block) as:  
````py  
TEMPLATE_DIR = path(BASE_DIR, 'templates') 
 ````  
* And after that in "TEMPLATES" section of "settings.py" under "DIRS : []" I pass variable as:  
````py 
 DIRS : [TEMPLATES_DIR] 
````
*  After that I run the server again and now my program running successfully.  

#### (And now I have to set my HTML code to make TODO App and make it's connection with Django.)

## HTML from  
* I pickup a HTML Form from bootsrat (W3school site) and replace it with the html code that I wrote in todo_2.html, and make changes in the html code accordingly.  
* After making changes like this:
```  
 <form action="{% url 'crt_todo' %}" method="POST">    
/* The "{% url 'ctr_todo' %}" used to generate the URL for the create_todo view with help of "name" variable in todo2/url.py.  */
                {%csrf_token%}
                <div class="form-group">
                    <label for="title">Title:</label>
                    <input type="text" class="form-control" id="title" placeholder="Enter title" name="title">
                </div>
                <div class="form-group">
                    <label for="description">Description</label>
                    <textarea class="form-control" id="description" name="description"></textarea>
                </div>
                <button type="submit" class="btn btn-dark">Submit</button>
            </form> 
````            
* We will do changes in 'todo_2/views.py' now. In 'todo_2/views.py' we will make a method/function "create_todo" .  
* And in this function we will pass request as: ` def create_todo(request):`  and after that we apply a `if` statement to check if the request method is "POST" it will access the title and description of the request.  
* And the code to access title and description is:  
````py
title=request.POST.get('title')
description=request.POST.get('description')
````    
* If we want to create database we will write:  
` TodoModel.objects.create(title:title,description:description)` and we also have to import the TodoModel method from todo_2/models.py as: `from .models import TodoModel` in todo_2/views.py .  
* The `return redirect(/todo2)` will used to take you to home page where the Todo form is after entering data, and we also have to import redirect.  
* The create_todo function in .views will we as:  
````py
def create_todo(request):
    if request.method==POST:
       title=request.POST.get('title')
       description=request.POST.get('description')
       TodoModel.objects.create(title=title,
       description=description)
    return redirect('/todo2')        
````  
* And after that now we have to pass 'create_todo' method (i.e. is in .views) in todo_2/url.py as:  
````
path('todo/create', views.create_todo, name='crt_todo')    # "name='crt_todo'" is used in todo_2.html as {% url 'ctr_todo' %}
````
## Display Todo table:  
* First we have to fetch todos in todo2/views.py file's todo_list function as: `todos = TodoModel.objects.get()`  
* Now we have to pass this "todos" variable in `return render(request, 'todo/todo_2.html')` as `return render(request, 'todo/todo_2.html', {'todos':todos})`
* And Now we will access this "todos" in frontend by creating table in todo_2.html file and add "complete" button in it as:  
```
<table class="table">
        <thead>
        <tr>
            <th>SNO.</th>
            <th>Title</th>
            <th>Description</th>
            <th>Action</th>
        </tr>
        </thead>
        <tbody>
        {% for todo in todos %}
        <tr>
            <td>{{forloop.counter}}</td>  /* it will show the serial number in the table*/
            <td>{{todo.title}}</td>
            <td>{{todo.description}}</td>
            <td>
                {% if todo.completed %}
                <span class="badge badge-success">Completed</span>
                {% else %}
                <a class="btn-sm btn-dark" href="{% url 'complete_todo' todo.id %}">Complete</a>
                {% endif %}
            </td>  /* The 'complete_todo' is a url of 'todo_2/views.py' file's method*/
        </tr>
        {% endfor %}
        </tbody>
    </table>
```  
* Now we have to create a 'complete_todo' method in 'todo_2/views.py' that will perform a action that show if the task is completed or not, the code will we as:  
```` py
def complete_todo(request, todo_id):
    todo = TodoModel.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('/todo2')
````  
* After that we have to give the link of this method/function in 'todo_2/urlss.py' as:
````py
path('todo/complete/<int:todo_id>', views.completed_todo, name='complete_todo')
````
##### To add "Delete" button/option in the table, we have to repeat the same procedure as complete, we just have to write delete instead of complete,
* The code of adding delte button/option will be as:  
  -  HTML:  
    ````
    <tbody>
        {% for todo in todos %}
        <tr>
            <td>{{forloop.counter}}</td>  /* it will show the serial number in the table*/
            <td>{{todo.title}}</td>
            <td>{{todo.description}}</td>
            <td>
                {% if todo.completed %}
                <span class="badge badge-success">Completed</span>
                {% else %}
                <a class="btn-sm btn-dark" href="{% url 'complete_todo' todo.id %}">Complete</a>
                {% endif %}
                <a class="btn-sm btn-danger" href="{% url 'delete_todo' todo.id %}">Delete</a>
            </td>  /* The 'delete_todo' is a url of 'todo_2/views.py' file's method*/
        </tr>
        {% endfor %}
        </tbody>
    ````   
    - .todo_2/views.py:  (Create 'delete_todo' method in 'views.py')
    ```` py
       def delete_todo(request,todo_id):
            todo = TodoModel.objects.get(id=todo_id)
            todo.delete()
            return redirect("/todo2")
    ````    
    - .todo_2/urls.py  (add 'delete_todo' method url in 'url.py')
    ````py
      path('todo/delete/<int:todo_id>', views.delete_todo, name = 'delete_todo')
    ````            
##### To add new items on the upward rows we have to add 'order_by(-id)' in 'todo_list' method of 'todo_2/views.py' as:  
```` py
def todo_list(request):
    todos = TodoModel.objects.order_by('-id')   #The 'order_by(-id)' instead of 'all()' will add todo items on upper row of table
    return render(request, 'todo2/todo_2.html', {'todos':todos})
````













