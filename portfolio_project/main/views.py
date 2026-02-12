from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def home_view(request): 
    return HttpResponse("<h1>Welcome to My Portfolio</h1>") 
def projects_view(request): 
    return HttpResponse("<h1>My Projects</h1>")