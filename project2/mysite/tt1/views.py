from unicodedata import name
from django.http import HttpResponse
from urllib import request
from django.shortcuts import get_object_or_404, render
from .models import Place,Manager

# Create your views here.
def home(request):
    return render(request,"home.html")
    #return HttpResponse("Hello, world. You're at the polls index.")

def work_place(request,name):
    placename= get_object_or_404(Place,pk=name)
    return HttpResponse("THIS IS THE WORK PLACE PAGE")
    

