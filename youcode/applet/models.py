from django.db import models

# Create your models here.
from django.db import models


class People(models.Model):
    name = models.CharField(max_length=200)
    signup_date = models.DateTimeField("date published")
    coins = models.IntegerField(default=0)


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    location = models.CharField
    instructor = People
    description = models.CharField(max_length=500)
    attendees = models.ManyToOneRel(field_name = "people" ,to=People)
    image = models.ImageField()