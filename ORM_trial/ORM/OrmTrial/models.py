from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField (max_length=50)
   
        
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    bio=models.TextField (max_length=50)

       
    

    
    


        
    