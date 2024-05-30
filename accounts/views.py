from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from sales.models import Customer

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
    
def register_page(request):
        return render(request, 'register.html')
    
def register(request):
        username = request.POST["inputUsername"]
        password1 = request.POST["inputPassword1"]
        password2 = request.POST["inputPassword2"]
        email = request.POST["inputEmail"]
        first_name = request.POST["inputFirstname"]
        last_name =request.POST["inputLastname"]
        phone =request.POST["inputPhone"]
        
        context = {
            'username' : username,
            'email' :email,
            'first_name' :first_name,
            'last_name' : last_name,
        }
        
        if password1 != password2:
            context.update(
                {
                    'error_message': 'Passwards must match. please try again'
                }
            )
            return render(request, 'register.html', context)
        
        if User.objects.filter(username=username).exists():
            context.update(
                {
                    'error_message': 'username exists'
                }
            )
            return render (request, 'register.html', context)
        
        user = User.objects.create_user(username=username, email=email, password=password1, first_name =first_name, last_name =last_name)
        user.save()
        customer = Customer.objects.create(first_name =first_name, last_name =last_name, email=email, user=user)
        customer.save()
        
        return render (request, 'login.html', context)
        
        
        
        
        
        
 
