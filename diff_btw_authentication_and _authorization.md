## **Difference Between Authentication and Authorization** 

| Feature           | Authentication | Authorization |
|------------------|---------------|--------------|
| **Definition**   | Verifies the identity of a user. | Determines what resources a user can access. |
| **Purpose**      | Confirms "Who you are?" | Confirms "What you can do?" |
| **Process**      | Usually involves username, password, OTP, biometrics, etc. | Involves setting permissions and access controls. |
| **When it happens?** | Before authorization. | After authentication. |
| **Example**      | Logging into an account with credentials. | Granting access to certain files based on user roles. |

## Create auth_app
* I cretaed a auth_app, using command: ``python manage.py startapp auth_app``  
## Settings  
* After cretaeing the app use inbuilt variable in django main project settings; like ,   
``` py
AUTHENTICATION_BACKENDS = [
    django.contrib.auth.backends.MOdelBackend
]
```