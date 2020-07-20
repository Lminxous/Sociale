from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=35)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    reported_by = models.ManyToManyField(User,blank=True, related_name="reported_by")

    def __str__(self):
        return self.title

        


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name='author',null=True,default='',on_delete=models.CASCADE)
    comment = models.CharField(max_length=80)

    def __str__(self):
        return self.comment