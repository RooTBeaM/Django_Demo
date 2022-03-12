from turtle import title
from django.contrib import admin
from .models import Blog


# Register your models here.
# admin.site.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    """"Register model by ModelAdmin"""
    list_display = ('title','post','date_created','date_updated')

admin.site.register(Blog, BlogAdmin)
