from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from django.contrib import admin
from .models import Artist, Work

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
    def __str__(self):
        return self.name
        
# add some dummy data


admin.site.register(Artist)
admin.site.register(Work)

# Add some dummy data
artist1 = Artist.objects.create(name='John Doe')
artist2 = Artist.objects.create(name='Jane Smith')

work1 = Work.objects.create(link='https://www.youtube.com/watch?v=dQw4w9WgXcQ', work_type='youtube')
work1.artist.add(artist1)

work2 = Work.objects.create(link='https://www.instagram.com/p/CQwfn3Dj4zg/', work_type='instagram')
work2.artist.add(artist2)

work3 = Work.objects.create(link='https://www.youtube.com/watch?v=ZVGfV5eG4xo', work_type='youtube')
work3.artist.add(artist1, artist2)



