from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'salary', 'employment_type', 'posted_by', 'date_posted')
    search_fields = ('title', 'location', 'description')
    list_filter = ('employment_type', 'date_posted')
    ordering = ('-date_posted',)

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'applied_at')
    search_fields = ('name', 'email', 'job__title')
    list_filter = ('job', 'applied_at')
    ordering = ('-applied_at',)
