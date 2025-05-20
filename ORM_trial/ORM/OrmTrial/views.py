# views.py
from django.shortcuts import render
from .forms import UserForm


def user_view(request):
    form = UserForm()
    return render(request, './orm/user.html', {'form': form})

# def user_login(request):
#         if request.method == 'POST':
#          form = UserCreationFOrm(data=request.POST)
        



    