from django.contrib.auth.models import User
from .models import Author
from django.db.models.signals import post_save #type of signal
from django.dispatch import receiver

#when the user is created i want to send a #signal# to the Author
#and Author receiving a signal will create a new user for the new author

@receiver(post_save, sender=User)
def create_user_author(sender, instance, created, **kwargs):
    #sender - the model(User)
   # instance - the model's instance that was create or saved (username = ola, password)
   #created - bool, True - just created, False - was already in the database
   
    if created: #just created = new
        Author.objects.create(user = instance, name = instance.username)
        
