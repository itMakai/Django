from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_page(request):
    return render(request, 'login.html')


def signin(request):
    username =request.POST.get("inputUsername")
    password =request.POST.get("inputPassword")

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return render(request, 'index.html')
    else:
        context = {'message': 'Login failed. Username or password incorrect. Please try again.'}
        return render(request, 'login.html', context)
 
