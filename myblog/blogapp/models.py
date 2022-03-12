from django.db import models

class Blog(models.Model): 
    title = models.CharField(max_length=120) 
    post = models.TextField() 
    date_created = models.DateTimeField() 
    date_updated = models.DateTimeField()

    def __str__(self):
        return self.title