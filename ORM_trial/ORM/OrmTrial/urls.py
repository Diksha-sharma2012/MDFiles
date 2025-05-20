from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_view, name='user'),
    path('user/', views.user_login, name='user-login')
]
