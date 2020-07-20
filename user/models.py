from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    about = models.CharField(default='',max_length=50,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Circle(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,default='',null=True,related_name='owner')
    friends = models.ManyToManyField(User,related_name='friends')

    def __str__(self):
        return self.owner.username
