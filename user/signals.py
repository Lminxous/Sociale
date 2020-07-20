from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,Circle

@receiver(post_save, sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()   

@receiver(post_save,sender=User)
def create_circle(sender,instance,created,**kwargs):
    if created:
        Circle.objects.create(owner=instance)
        # circle = Circle.objects.get(owner=instance)
        # circle.friends.add(owner)

      
# @receiver(post_save,sender=User)
# def create_circle(sender,instance,created,**kwargs):
#     if created:
#         Circle.objects.create(owner=instance)
#         circle = Circle.objects.get(owner=instance)
#         friends = circle.friends.all() 
#         circle.friends.add(owner)
#         instance.circle.save() 
     
