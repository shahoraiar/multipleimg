from django.db import models

# Create your models here.
class Mutlipleimg(models.Model) : 
    images = models.FileField()