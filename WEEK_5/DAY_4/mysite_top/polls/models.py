from django.db import models

# Create your models here.

class Post(models.Model):
    # id = models. - not needed, creates in authomatically
   
    title = models.CharField(max_length=50)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)  #once we've added and you post - the date time of creation will be exact
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    #migration - instruction for the database about changes(adding a table, changing a column)
    
class Author(models.Model):
    name = models.CharField(max_length=50) #by default null not allowed
    email = models.EmailField(blank=True, null=True) #blank don't have to provide value
    
#create a view where we get all of the posts of a certain author that return an HTTPresponse with all of the post of a certain author
