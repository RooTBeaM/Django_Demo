from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('all-test', views.all_test, name='test'),
    path('query-data', views.query_data, name='query'),
]