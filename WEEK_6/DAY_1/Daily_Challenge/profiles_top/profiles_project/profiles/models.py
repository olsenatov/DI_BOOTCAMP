from django.db import models

# Create your models here.
# model named Profile with the fields name (CharField), email (EmailField), and is_active (BooleanField, default=True).
# Don’t forget to add the profiles app to the INSTALLED_APPS list in your settings file (settings.py) and run migrations to create the Profile table in the database.

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    