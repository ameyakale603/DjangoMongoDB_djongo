from django.db import models

# Create your models here.

class FormModel(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    text = models.CharField(max_length=1000)

