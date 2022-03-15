from distutils.command.upload import upload
from django.db import models

class Blog(models.Model): 
    title = models.CharField(max_length=120) 
    post = models.TextField() 
    date_created = models.DateTimeField(auto_now_add=True) 
    date_updated = models.DateTimeField(auto_now=True)

    #link show image
    #need python -m pip install Pillow
    #need type python manage.py makemigrations
    #save to database by python manage.py migrate
    feild_img = models.ImageField(upload_to='featured_img', blank=True)

    def __str__(self):
        return self.title