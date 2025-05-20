##  Superuser login error
* ERROR-  `django.db.utils.OperationalError: no such table: auth_user`  
* Run command o solve error - `python manage.py migrate --run-syncdb` (You have to migrate first before creating superuser.)


## Apps are not loaded ( or apps are not installed)  
* If this error occurs then run `set DJANGO_SETTINGS_MODULE=auth.settings` and after that run the server.

## When image is not found:
* If the image not found using `{% static 'image_name' %}` method, then check if the image is present in "static" folder or not.
* If the image is not present in static folder then you don't need to apply "static" method on it.