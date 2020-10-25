from django.db import models
from datetime import datetime
# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=40)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')