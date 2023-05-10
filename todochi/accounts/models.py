from django.db import models
from django.contrib.auth.models import User
# Create your models here.


    
# class MainUser(AbstractUser):
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    birthday = models.DateField(auto_now=False, blank=True ,null=True)
    image = models.ImageField(upload_to='user_images/', blank=True)
    bio = models.TextField()    
    
    def __str__(self):
        return str(self.user.username)