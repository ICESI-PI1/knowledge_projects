from django.db import models
from Auth.models import User 


class State(models.Model):
    state_id=models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=30)
    description = models.TextField()
    def __str__(self):
        return self.state_name

class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name = models.TextField(max_length=30)
    icon_src = models.TextField(max_length=30)
    description = models.TextField()
    def __str__(self):
        return self.category_name
    

class Convocatory(models.Model):
    #Primary key
    convocatory_id = models.AutoField(primary_key=True)
    convocatory_name = models.CharField(max_length=30)
    start_date = models.DateField()
    closing_date = models.DateField()
    def __str__(self):
        return self.convocatory_name

class Project(models.Model):
    #Primary key
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50)
    project_description = models.TextField()
    result = models.TextField()
    scope = models.TextField()
    work_plan = models.TextField()
    budget = models.DecimalField(max_digits=10,decimal_places=0)
    goal = models.TextField()
    state =models.ForeignKey(State,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.FileField(upload_to="pic/%y/",default="")
    convocatory = models.ForeignKey(Convocatory,on_delete=models.SET_NULL, blank=True, null = True)
    def __str__(self):
        return self.project_name
    class Meta :
        ordering=('-project_id',)

class Binnacle(models.Model):
    #Primary key
    binnacle_id = models.CharField(max_length=5)
    #Foreing key
    project_id = models.ForeignKey(Project,on_delete = models.CASCADE)

class Log(models.Model):
    #Primary key
    log_id = models.CharField(max_length=10)

    log_name = models.CharField(max_length=30)
    date_time = models.DateTimeField()
    observations = models.TextField()
    results = models.TextField()
 
    #Foreing Key
    binnacle_id = models.ForeignKey(Binnacle,models.CASCADE)

class Donation(models.Model):
    donation_id= models.AutoField(primary_key=True)
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10,decimal_places=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)


