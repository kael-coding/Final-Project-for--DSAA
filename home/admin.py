from django.contrib import admin
from .models import Job
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'salary', 'employment_type')
    search_fields = ['title', 'location']
    list_filter = ['employment_type']

admin.site.register(Job, JobAdmin)