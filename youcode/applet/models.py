from django.db import models

# Create your models here.
from django.db import models


class People(models.Model):
    name = models.CharField(max_length=200)
    signup_date = models.DateTimeField("date published")
    coins = models.IntegerField(default=0)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

