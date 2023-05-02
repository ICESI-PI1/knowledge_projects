from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
    

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Client')

    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    representative_name = models.CharField(max_length=30)
    phone_number_representative = models.CharField(max_length=20)

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Employee')

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField()
    birth_date = models.DateField()
