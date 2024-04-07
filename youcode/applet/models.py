from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, AbstractUser, BaseUserManager

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    coins = models.IntegerField(default=0)



class People(models.Model):
    name = models.CharField(max_length=200)
    signup_date = models.DateTimeField("date published")
    coins = models.IntegerField(default=0)

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField("Event date", default= datetime.now)
    location = models.CharField(max_length=200)
    instructor = models.CharField(max_length=200)  
    # Specify a unique related_name for instructor
    description = models.CharField(max_length=500)
    attendees = models.ManyToManyField(User, related_name='attended_events',  blank=True)  
    # Specify a unique related_name for attendees
    image = models.ImageField(upload_to='event_images/')
    coins = models.IntegerField(default=0)

class Prize(models.Model):
    image = models.ImageField(upload_to='prize_images/')
    prize_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    is_sold = models.BooleanField()
    
    