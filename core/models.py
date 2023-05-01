from django.db import models


class State(models.Model):
    state_name = models.CharField(max_length=30)
    description = models.TextField()

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    description = models.TextField()

class Project(models.Model):
    #Primary key
    project_id = models.CharField(primary_key=True,max_length=5)

    project_name = models.CharField(max_length=50)
    project_description = models.TextField()
    result = models.TextField()
    scope = models.TextField()
    work_plan = models.TextField()
    budget = models.DecimalField(max_digits=10,decimal_places=0)
    goal = models.TextField()

    
    state =models.ForeignKey(State,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

      
class Convocatory(models.Model):
    #Primary key
    convocatoryId = models.CharField(max_length=5)

    start_date = models.DateField()
    closing_date = models.DateField()

    #Foreign key
    project = models.ForeignKey(Project,models.CASCADE)

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
    


