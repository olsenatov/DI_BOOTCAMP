from django.db import models

# Create your models here

CATEGORIES = [
    ('sci', 'scientific'), #left goes to the database, right - presented
    ('na', 'nature')
    
]

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=3, choices = CATEGORIES, default = None )
    
    def __str__(self):
        return f'{self.title} - {self.id}'
    
    