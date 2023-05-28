import datetime
import time
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    is_customer=models.BooleanField('is customer', default=False)# 'is customer' is try
    is_translator=models.BooleanField('is translator', default=False)# 'is customer' is try
    is_Admin=models.BooleanField('is Admin', default=False)# 'is customer' is try
    
    

class Translator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,
    primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)   
    phoneNumber = models.CharField(max_length=17)
    First_Language = models.CharField(max_length=3)
    Second_Language = models.CharField(max_length=3)
    price = models.IntegerField(null=False, default=0)
    Certification = models.CharField(max_length=4)
    
    
class Translatorr(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,
    primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)   
    phoneNumber = models.CharField(max_length=17)
    First_Language = models.CharField(max_length=3)
    Second_Language = models.CharField(max_length=3)
    price = models.IntegerField(null=False, default=0)
    numberOfAppointment=models.IntegerField(null=False, default=0)
    Certification = models.CharField(max_length=4)
    rate= models.IntegerField(default=0)
    numberOfAppointment=models.IntegerField(null=False, default=0)
    Bio = models.CharField(max_length=200, blank=True)
    gender= models.CharField(max_length= 10,default='null')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    First_Language = models.CharField(max_length=3)
    phoneNumber = models.CharField(max_length=17)
    Bio = models.CharField(max_length=200, blank=True)
    gender= models.CharField(max_length= 10,default='null')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=17)
    gender= models.CharField(max_length= 10,default='null')


class Appointment(models.Model):
    customerName = models.CharField(max_length=50)
    translatorName = models.CharField(max_length=50)
    customerID = models.CharField(max_length=200)
    translatorID = models.CharField(max_length=200)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.IntegerField(default=0)
    fromLanguage = models.CharField(max_length=200)
    toLanguage = models.CharField(max_length=200)
    paid = models.BooleanField(default=False)
    paidTime = models.DateTimeField(null=True, blank=True)

    #ِSend request

