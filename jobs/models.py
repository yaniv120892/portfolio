from django.db import models

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    short_info = models.CharField(max_length=100)
    long_info = models.CharField(max_length=500)

    def __str__(self):
        return self.title
