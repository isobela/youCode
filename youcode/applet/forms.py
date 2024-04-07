from django import forms
from .models import Event
from .models import Prize

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'location', 'description',  'image', 'coins']

