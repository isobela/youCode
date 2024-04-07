from django.shortcuts import render, redirect
from .forms import EventForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Prize
from .models import Event, UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
            form.save()
            return redirect('home')  # Redirect to event list page
    else:
        form = EventForm()
    return render(request, 'upload.html', {'form': form})

def prize_list(request):
    prizes = Prize.objects.all()
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    return render(request, 'prize_list.html', {'prizes': prizes, 'userprofile': user_profile})

def about_us(request):
    return render(request, 'about_us.html')

def home(request):
    events = Event.objects.all()
    return render(request, 'home2.html', {'events': events})

def event_display(request, event):
    return render(request , 'event.html', {'event': event} )
    


