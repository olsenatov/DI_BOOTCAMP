from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey("Vehicle_Type", on_delete=models.CASCADE)
    date_created = models.DateField()
    real_cost = models.DecimalField(max_digits=10, decimal_places = 2)
    size = models.ForeignKey("Vehicle_Size", on_delete=models.CASCADE)
    
class Vehicle_Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Vehicle_Size(models.Model):
    name = models.CharField(max_length = 50, unique = True)

class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)

class Rental_Rate(models.Model):
    daily_rate = models.DecimalField(max_digits=5, decimal_places=2)
    vehicle_type = models.ForeignKey('Vehicle_Type', on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey('Vehicle_Size', on_delete=models.CASCADE)

class Rantal_Station(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    address = 
    

RentalStation:

name: CharField (max_length=100)
capacity: IntegerField
address: ForeignKey to Address

Address:

address: CharField (max_length=100)
address2: CharField (max_length=100, null=True, blank=True)
city: CharField (max_length=50)
country: CharField (max_length=50)
postal_code: CharField (max_length=10)

VehicleAtRentalStation:

arrival_date: DateField
departure_date: DateField (null=True, blank=True)
vehicle: ForeignKey to Vehicle
