from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    is_client = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

  
    def save(self,*args, **kwargs):
        if not self.pk and not  self.is_superuser:
            self.set_password(self.password)
            return super(User, self).save(*args, **kwargs)
        if self.is_superuser:
            return super().save(*args, **kwargs)
       
        
class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Client')

    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    representative_name = models.CharField(max_length=30)
    phone_number_representative = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Employee')

    img=models.FileField(upload_to="pic/%y/",default="")

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    def __str__(self):
        return self.user
