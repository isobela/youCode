# accounts/urls.py
from django.urls import path
from .views import SignUpView,  upload_event, home
from .views import prize_list


urlpatterns = [
     path("", home, name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
     path('upload-event/', upload_event, name='upload_event'),
     path("prizes/", prize_list, name='prize_list')

]