from django.db import models

# Create your models here.

class Hotel(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    owner=models.CharField(max_length=255,null=True,blank=True)
    rating=models.IntegerField(default=0)
    location=models.CharField(max_length=255,null=True,blank=True)
    image1=models.CharField(max_length=255,null=True,blank=True)
    image2=models.CharField(max_length=255,null=True,blank=True)
    image3=models.CharField(max_length=255,null=True,blank=True)