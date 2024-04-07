from django import forms
from .models import Event
from .models import People
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    instructor = forms.ModelChoiceField(queryset= User.objects.all(), empty_label=None)
    class Meta:
        model = Event
        fields = ['event_name', 'event_date',  'location', 'description',  'image', 'coins', 'instructor']

class EventSearchForm(forms.Form):
    query = forms.CharField(label='Search for events', max_length=100)
