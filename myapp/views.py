from django.shortcuts import render
from .models import Settings

def index(request):
    settings = Settings.objects.first()
    return render(request, 'homepage.html', {'settings': settings})