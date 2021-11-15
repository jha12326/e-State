from django.db import models

# Create your models here.
class Customer(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    age = models.CharField(max_length=20)
    con = models.CharField(max_length=20)
    add = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=20)
    post= models.CharField(max_length=20)
    skill = models.CharField(max_length=20)
    ho1 = models.CharField(max_length=20)
    ho2 = models.CharField(max_length=20)
    ho3 = models.CharField(max_length=20)
  

