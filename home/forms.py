from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Job, JobApplication

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary', 'employment_type', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'employment_type': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("The image file is too large. Maximum size is 5MB.")
        return image

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job', 'name', 'email', 'cover_letter', 'resume']

    job = forms.ModelChoiceField(queryset=Job.objects.all(), widget=forms.HiddenInput())  
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    cover_letter = forms.CharField(widget=forms.Textarea)
    resume = forms.FileField()


    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if resume.size > 10 * 1024 * 1024:  # Limit file size to 10MB
                raise forms.ValidationError("File size must be under 10MB.")
        return resume