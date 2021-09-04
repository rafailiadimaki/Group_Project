from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'e-shop/signup.html', {'form': form})

def login_user(request):
    errors={}
    if request.method == 'POST':
        username = request.POST ['username']
        password = request.POST ['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            if not username:
                errors['empty_username'] ='Please enter username'
            elif not password:
                errors['empty_password'] ='Please enter password'
            elif user is None:
                errors['invalid'] = 'Username and password do not match'
    return render(request, 'e-shop/login.html', errors)

def logout_user(request):
    logout(request)
    return render(request, 'e-shop/logout.html', {})
