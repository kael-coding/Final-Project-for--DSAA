from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_index, name= 'index'),
    path('jobs/', views.front_jobs, name= 'jobs'),
    path('post-job/', views.front_post_jobs, name= 'post_jobs'),
    path('contact/', views.front_contact, name= 'contact'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
