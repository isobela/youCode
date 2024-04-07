from django.shortcuts import render, redirect
from .forms import EventForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Prize
from .models import Event
from PIL import Image


def home(request):
    return render(request, template_name='home2.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def upload_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event_name = form.cleaned_data["event_name"]
            event_date = form.cleaned_data["event_date"]
            location = form.cleaned_data["location"]
            instructor = form.cleaned_data["instructor"]
            description = form.cleaned_data["description"]
            image = request.FILES["image"]
           
        
            coins = form.cleaned_data["coins"]
            event = Event.objects.create(event_name = event_name, event_date = event_date,location= location,
                                 instructor=  instructor,  description = description, image = image, coins =  coins)
            event.save()
            return redirect('home')  # Redirect to event list page
    else:
        form = EventForm()
    return render(request, 'upload.html', {'form': form})

def prize_list(request):
    prizes = Prize.objects.all()
    return render(request, 'prize_list.html', {'prizes': prizes})

def about_us(request):
    return render(request, 'about_us.html')


