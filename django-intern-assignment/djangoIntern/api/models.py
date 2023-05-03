from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IG'
    OTHER = 'OT'
    WORK_TYPE_CHOICES = [
        (YOUTUBE, 'Youtube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    ]
    link = models.URLField()
    work_type = models.CharField(
        max_length=2,
        choices=WORK_TYPE_CHOICES,
        default=OTHER,
    )

class Artist(models.Model):
    name = models.CharField(max_length=255)
    work = models.ManyToManyField(Work)

