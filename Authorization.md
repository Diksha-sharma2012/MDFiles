## Authorization
* For Authorization add :  
``py 
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login' ``  
in setting.py  
* And after that import `from django.contrib.auth.decorators import login_required` in app's views.py and then apply the `@login_required` decorator on the function on which you want to apply login required function.



* The decorator is used in `views.py`, in functions of this file it used as "@auth". But if the classes are created in `views.py` then you have to import `from django.utils.decorators import method_decorator` and use it on the top of class as `@method_decorator(auth, name='dispatch')`