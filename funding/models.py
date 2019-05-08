from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    isAdmin = models.BooleanField(default=0)
    phone = models.CharField(max_length=11)
    birth_date = models.DateField()
    fb_account =models.CharField(max_length=300)
    country = models.CharField(max_length=60)
    img = models.ImageField()

    def __str__(self):
        return self.first_name

class Project(models.Model):
    title = models.CharField(max_length=100)
    detials = models.CharField(max_length=600)
    start_date = models.DateField()
    end_date = models.DateField()
    target= models.FloatField()
    achived =models.FloatField()
    img = models.ForeignKey('Project_Image',on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title       

class Project_Image(models.Model):
    img = models.ImageField()   
