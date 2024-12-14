from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import SignUpForm, LoginForm, JobForm
from django.contrib import messages
from .models import Job

#for the frontpage
@login_required
def front_index(request):
    return render(request, 'frontpage/index.html')
@login_required
def front_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'frontpage/jobs.html',{'jobs': jobs})

@login_required
def front_post_jobs(request):
    form = JobForm()
    return render(request, 'frontpage/post-jobs.html', {'form': form})

@login_required
def front_contact(request):
    return render(request, 'frontpage/contact.html')





#for the succese login
def Succes_jobs(request):
    jobs = Job.objects.all() 
    return render(request, 'home/jobs.html', {'jobs': jobs})

def Succes_post_jobs(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user  
            job.save()
            return redirect('Sjobs')  
    else:
        form = JobForm()
    return render(request, 'home/post-jobs.html', {'form': form})

def Succes_contact(request):
    return render(request, 'home/contact.html')

def Succes_home(request):
    return render(request, 'home/index.html')

def profile_view(request):
    return render(request, 'home/profile.html', {'username': request.user.username})






#for the user login
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
