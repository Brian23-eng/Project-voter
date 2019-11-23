from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import  ImageField
import datetime as dt


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' )
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio",  blank=True)
    name = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=120, blank=True)
    contact = models.CharField(max_length=120, blank=True)



class Post(models.Model):
    title = models.CharField(max_length=150)
    url = models. CharField(max_length=255)
    description = models.TextField(max_length=500)
    technologies = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='project_images', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateField(auto_now_add=True, blank=True)
    
    
class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)

