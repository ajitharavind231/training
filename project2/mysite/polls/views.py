from django.shortcuts import  render
from django.http import HttpResponse

def home(request):
    return render(request,"test.html",{ "name" : "achu" } )


# Create your views here.
