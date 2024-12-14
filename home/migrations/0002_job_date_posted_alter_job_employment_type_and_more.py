# Generated by Django 5.1.4 on 2024-12-14 18:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='employment_type',
            field=models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time'), ('CT', 'Contract'), ('FL', 'Freelance'), ('IT', 'Internship')], default='FT', max_length=2),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
