from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=200)
