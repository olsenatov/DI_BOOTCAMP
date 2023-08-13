from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    # id = models. - not needed, creates in authomatically
   
    title = models.CharField(max_length=50)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)  #once we've added and you post - the date time of creation will be exact
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    #migration - instruction for the database about changes(adding a table, changing a column)

#one to many    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=50) #by default null not allowed
    email = models.EmailField(blank=True, null=True) #blank don't have to provide value
    
    
#many to many#
class Category(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField('Post', related_name = 'categories')
    
    def clean_name(self):  #models validation
        print('Cleaning the Name')
        if 'conspiracy' == self.name:
            raise ValidationError(f"Can't have conspiracy in category name")
    
        return self.name
    
#one to one - #password

class Profile(models.Model):
    author = models.OneToOneField('Author', on_delete = models.CASCADE)
    image_urls = models.URLField(blank = True, null = True)

#models validation
#conspiracy - to exclude

#authentication system

