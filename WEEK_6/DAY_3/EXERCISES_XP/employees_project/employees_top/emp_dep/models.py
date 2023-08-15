from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    salary = models.FloatField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    projects = models.ManyToManyField('Project', related_name='employees')
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

