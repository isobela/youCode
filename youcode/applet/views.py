from django.shortcuts import render

def my_html_view(request):
    return render(request, 'home.html')
