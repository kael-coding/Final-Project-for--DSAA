from django.contrib.auth.models import User
from django.db import models

class Job(models.Model):
    EMPLOYMENT_TYPES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
        ('Internship', 'Internship'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPES)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    date_posted = models.DateTimeField(auto_now_add=True)
   
    image = models.ImageField(upload_to='job_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)  # Auto-filled on create

    def __str__(self):
        return f'{self.applicant.username} - {self.job.title}'
