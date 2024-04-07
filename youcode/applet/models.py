from django.db import models

class People(models.Model):
    name = models.CharField(max_length=200)
    signup_date = models.DateTimeField("date published")
    coins = models.IntegerField(default=0)

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    instructor = models.ForeignKey(People, on_delete=models.CASCADE, related_name='instructed_events')  
    # Specify a unique related_name for instructor
    description = models.CharField(max_length=500)
    attendees = models.ManyToManyField(People, related_name='attended_events')  
    # Specify a unique related_name for attendees
    image = models.ImageField(upload_to='event_images/')
    coins = models.IntegerField(default=0)

class Prize(models.Model):
    image = models.ImageField(upload_to='prize_images/')
    prize_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    is_sold = models.BooleanField()
    
    