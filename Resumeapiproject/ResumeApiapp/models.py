from django.db import models

# Create your models here.
#creating resume api model
class Resumeapi(models.Model):
    name = models.CharField(max_length=30)
    graduation = models.CharField(max_length=30)
    skills = models.CharField(max_length=100)
    experience = models.FloatField()
    aboutus = models.CharField(max_length=200)
    resume = models.CharField(max_length=500)
