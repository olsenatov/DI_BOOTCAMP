from django.db import models
from django.contrib.auth.models import User

# Create your models here.
WEATHER_TYPES = [
    ('su', 'sunny'),
    ('clo', 'cloudy'),
    ('wi', 'windy'),
    ('ra', 'rainy')
]
class Report(models.Model):
    forecaster = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    temperatute = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3, choices=WEATHER_TYPES)
    
    def __str__(self):
        return f'{self.location} - {self.id}'