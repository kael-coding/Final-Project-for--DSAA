from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_index, name= 'index'),
    path('jobs/', views.front_jobs, name= 'jobs'),
    path('post-job/', views.front_post_jobs, name= 'post_jobs'),
    path('contact/', views.front_contact, name= 'contact'),

    path('Sjobs/', views.Succes_jobs, name= 'Sjobs'),
    path('Spost-job/', views.Succes_post_jobs, name= 'Spost_jobs'),
    path('Scontact/', views.Succes_contact, name= 'Scontact'),

    path('home/', views.Succes_home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
