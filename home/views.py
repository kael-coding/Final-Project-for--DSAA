from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm, JobForm, JobApplicationForm
from django.contrib import messages
from .models import Job

#for the frontpage
def front_index(request):
    return render(request, 'front-page/index.html')


def front_jobs(request):
     context = {
        'jobs': Job.objects.all(),
        'is_logged_in': request.user.is_authenticated, 
    }
     return render(request, 'front-page/jobs.html', context)


def front_post_jobs(request):
    form = JobForm()
    return render(request, 'front-page/post-jobs.html', {'form': form})

def front_contact(request):
    return render(request, 'front-page/contact.html')



def Succes_jobs(request):
    jobs = Job.objects.all() 
    if request.method == 'POST' and 'apply' in request.POST:
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_id = request.POST.get('job_id') 
            if job_id:
                job = get_object_or_404(Job, id=job_id)  
                job_application = form.save(commit=False)
                job_application.applicant = request.user  
                job_application.job = job  
                job_application.save()
                messages.success(request, "Your application has been submitted successfully.")
                return redirect('Sjobs')  
            else:
                return HttpResponse("Job ID is missing.")
        else:
            return HttpResponse("There was an error with your application.")
    else:
        form = JobApplicationForm()

   
    return render(request, 'home/jobs.html', {'jobs': jobs, 'form': form})


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
    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
