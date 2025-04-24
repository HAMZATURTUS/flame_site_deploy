from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Blog

# Create your views here.

def index(request):
    return render(request, "flame_site/base.html")

def home(request):
    
    return render(request, "flame_site/home.html")