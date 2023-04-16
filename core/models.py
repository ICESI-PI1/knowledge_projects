from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.hashers import make_password,check_password
from django.conf import settings

class ClientManager(BaseUserManager):
    def create_user(self,nit, password = None):

        
        if not nit:
            raise ValueError('Theres is no a nit')
        user = self.model(nit=nit)
        user.set_password(password)
        user.save(using=self._db)
        return user
        

class Client(AbstractBaseUser):
    #Primary keiy
    nit = models.CharField(primary_key=True,max_length=11)
    name = models.CharField(max_length=30,null=False)
    phoneNumber = models.CharField(max_length=20)
    adress = models.CharField(max_length=20)
    representativeName = models.TextField()
    phoneNumberRepresentative = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'nit'
    manager = ClientManager() 
    
    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        return check_password(password, self.password)
    

class Project(models.Model):
    #Primary key
    projectId = models.CharField(primary_key=True,max_length=5)
    #Foreing Key
    nit = models.ForeignKey(Client,on_delete = models.CASCADE)

    name = models.CharField(max_length=30)
    description = models.TextField()
    result = models.TextField()
    scope = models.TextField()
    workPlan = models.TextField()
    budget = models.DecimalField(max_digits=10,decimal_places=0)
    humanCapital = models.TextField()
    state = models.CharField(max_length=20)
    goal = models.TextField()
    asssignedResources = models.TextField()
    category = models.CharField(max_length=20)
    convocatoryNumber = models.IntegerField()

  
    
class Convocatory(models.Model):
    #Primary key
    convocatoryId = models.CharField(max_length=5)
    #Foreign key
    projectId = models.ForeignKey(Project,models.CASCADE)
    startDate = models.DateField()
    closingDate = models.DateField()

class Binnacle(models.Model):
    #Primary key
    binnacleId = models.CharField(max_length=5)
    #Foreing key
    projectId = models.ForeignKey(Project,on_delete = models.CASCADE)

class Log(models.Model):

    #Primary key
    logId = models.CharField(max_length=10)
    #Foreing Key
    binnacleId = models.ForeignKey(Binnacle,models.CASCADE)
    
    dateTime = models.DateTimeField()
    observations = models.TextField()
    results = models.TextField()

class Rol(models.Model):
    name = models.CharField(primary_key=True,max_length=20)

class Employee(models.Model):
    #Primary key
    id = models.CharField(primary_key=True,max_length=10)

    #Foreign key
    role  = models.ForeignKey(Rol,on_delete = models.CASCADE)


    fullName = models.TextField()
    picture = models.ImageField()
    birthDate = models.DateField()


# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=150)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    investment= models.DecimalField(decimal_places=2,max_digits=10)
    investorNum=models.IntegerField()
    organization=models.TextField()
    img=models.FileField(upload_to="pic/%y/")
    def __str__(self):
        return self.title
    class Meta :
        ordering=('-id',)
    


