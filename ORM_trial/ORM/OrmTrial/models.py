from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField    