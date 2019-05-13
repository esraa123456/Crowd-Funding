from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    isAdmin = models.BooleanField(default=0)
    phone = models.CharField(max_length=11)
    birth_date = models.DateField(null=True, blank=True)
    fb_account =models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=60,null=True, blank=True)
    img = models.ImageField()
    projects = models.ManyToManyField('Project', through = 'Donation')
    def __str__(self):
        return self.first_name

class Project(models.Model):
    title = models.CharField(max_length=100)
    detials = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    target= models.FloatField()
    achived =models.FloatField()
    isFeatured = models.BooleanField(default=0)
    creator = models.ForeignKey('User',on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title       

class Project_Image(models.Model):
    img = models.ImageField()  
    project = models.ForeignKey('Project',on_delete=models.CASCADE, null=True)


class Category(models.Model):
    name = models.CharField(max_length=70)    

class Donation(models.Model):
    amount = models.FloatField()    
    user = models.ForeignKey('User',on_delete=models.CASCADE, null=True)
    project = models.ForeignKey('Project',on_delete=models.CASCADE, null=True)


class Comment (models.Model):
    body = models.CharField(max_length=1000)    
    user = models.ForeignKey('User',on_delete=models.CASCADE, null=True)
    project = models.ForeignKey('Project',on_delete=models.CASCADE, null=True)

class Project_Reports(models.Model):
    body = models.CharField(max_length=1000)    
    user = models.ForeignKey('User',on_delete=models.CASCADE, null=True)
    project = models.ForeignKey('Project',on_delete=models.CASCADE, null=True)


class Comment_Reports(models.Model):
    body = models.CharField(max_length=1000)    
    user = models.ForeignKey('User',on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey('Comment',on_delete=models.CASCADE, null=True)

# we often will use libraries for the next 2 classes so no need to define them now

# class Tag(models.Model):

# class Rate(models.Model):        
          
