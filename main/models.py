from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50,unique = True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    brand = models.CharField(max_length=50)
    phone = models.IntegerField()



    def set_password(self, password):
        self.password = make_password(password)
        
    def check_password(self, password):
        return check_password(password,self.password)
    
    def __repr__(self):
        return '<Seller {}>'.format(self.username)

    def __str__(self):
        return self.name

class Product(models.Model):
    choice=((1,'Uncategorized'),(2,'Beauty and Personal Care'),(3,'Wooden Utensils'),(4,'Stationary'),(5,'Clay Pots'))
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)
    category = models.PositiveSmallIntegerField(choices=choice, default=3)
    name= models.CharField(max_length=250)
    description=models.CharField(max_length=3500)
    price=models.IntegerField()
    image=models.ImageField(upload_to='products',blank=True)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()