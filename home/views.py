from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import SignUpForm, LoginForm
from django.contrib import messages

def front_index(request):
    return render(request, 'frontpage/index.html')

def front_jobs(request):
    return render(request, 'frontpage/jobs.html')

def front_post_jobs(request):
    return render(request, 'frontpage/post-jobs.html')

def front_contact(request):
    return render(request, 'frontpage/contact.html')

def home(request):
    return render(request, 'home/index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials')
    else:
        form = LoginForm()
    return render(request, 'home/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
