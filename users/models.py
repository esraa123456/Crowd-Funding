from django.db import models
from django.contrib.auth.models import User
# Create your models here
        
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=11,default='01234567890')
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class UserProfile (models.Model):
    user = models.OneToOneField(UserProfileInfo,on_delete=models.CASCADE )
    birth_date = models.DateField(null=True, blank=True)
    fb_account =models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=60,null=True, blank=True)


