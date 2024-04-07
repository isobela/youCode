from django.shortcuts import render, redirect
from .forms import EventForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Prize
from .models import Event
from django.contrib.auth.models import User


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
    return render(request, 'prize_list.html', {'prizes': prizes})

def about_us(request):
    return render(request, 'about_us.html')

<<<<<<< HEAD
=======

>>>>>>> 33dbd5dceeebfa6c5c380f11f4e0a9cf0f8839aa

