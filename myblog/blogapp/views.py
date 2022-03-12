from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def home(request):
    today = datetime.now()
    return render(request, "blogapp/home.html", {'today':today})

def about(request):

    return render(request, "blogapp/about.html")