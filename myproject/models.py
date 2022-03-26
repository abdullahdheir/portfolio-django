from django.db import models

# Create your models here.
class MyData(models.Model):
    name = models.CharField(max_length=100,default='')
    age = models.CharField(max_length=10,default=22)
    phone = models.CharField(max_length=30,default='')
    email = models.EmailField(max_length=45,default='')
    address = models.CharField(max_length=45,default='')
    degree = models.CharField(max_length=40,default='')
    specialty = models.CharField(max_length=30,default='')
    website = models.CharField(max_length=40,default='')
    freelance = models.BooleanField(max_length=20,default=True)
