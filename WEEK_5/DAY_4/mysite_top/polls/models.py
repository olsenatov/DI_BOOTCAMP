from django.db import models

# Create your models here.

class Post(models.Model):
    # id = models. - not needed, creates in authomatically
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)  #once we've added and you post - the date time of creation will be exact
    
    #migration - instruction for the database about changes(adding a table, changing a column)
    
    