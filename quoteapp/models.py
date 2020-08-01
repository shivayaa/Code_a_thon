from django.db import models

# Create your models here.

class Quotes(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(s):
        return s.title

