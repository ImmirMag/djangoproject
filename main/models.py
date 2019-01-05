from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key='True',)
    date = models.DateTimeField(blank='True',default='0000-00-00 00:00:00')
    name = models.TextField(max_length=20,default='Not')
    surname = models.TextField(max_length=20,default='Not')
    fathername = models.TextField(max_length=20,default='Not')
    description = models.TextField(max_length=200,default='Not')
    phone = models.TextField(max_length=20,default='Not')


# Create your models here.
