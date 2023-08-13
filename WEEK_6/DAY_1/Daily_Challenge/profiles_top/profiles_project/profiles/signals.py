
from .models import Profile
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

@receiver(post_save, sender=Profile)
def notify_new_profile(sender, instance, created, **kwargs):
    if created: 
        print(f'New profile created - Name: {instance.name} , email: {instance.email}')
        
@receiver(pre_delete, sender=Profile)        
def warn_before_deleting(sender, instance, **kwargs):
    if instance.is_active:
        print("Warning, the profile is active, delete?")
        #output in shell? Warning, the profile is active, delete? (1, {'profiles.Profile': 1})
        