# views.py
from django.shortcuts import render
from .forms import UserForm

def user_view(request):
    form = UserForm()
    return render(request, './orm/user.html', {'form': form})
