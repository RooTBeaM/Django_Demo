from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import Blog
# Create your views here.

def home(request):
    today = datetime.now()
    posts = Blog.objects.all()
    return render(request, "blogapp/home.html", {'today': today,
                                                'posts':posts})

def about(request):

    return render(request, "blogapp/about.html")

def all_test(request):

    return render(request, "blogapp/all_test.html")

def query_data(request):
    today = datetime.now()

    posts = Blog.objects.all()
    single_row = Blog.objects.get(pk = 3)
    rows = Blog.objects.all()[1:3]
    reversed_posts = Blog.objects.order_by('-id')
    columns = Blog.objects.values('title', 'id')
    first_row = Blog.objects.first()
    last_row = Blog.objects.last()


    return render(request, "blogapp/query_data.html", {'today': today, 
                                                'posts' : posts, 
                                                'single_row': single_row,
                                                'rows': rows,
                                                'reversed_posts' : reversed_posts,
                                                'columns': columns,
                                                'first_row': first_row,
                                                'last_row': last_row
                                                })

def post_details(request, id):
    today = datetime.now()
    single_row = Blog.objects.get(pk=id)
    return render(request, "blogapp/post_details.html", {'single_row':single_row, 'today':today})