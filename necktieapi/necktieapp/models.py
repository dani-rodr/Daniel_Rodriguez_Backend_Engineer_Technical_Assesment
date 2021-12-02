from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Fee(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    daysIncludingWesternMeds = models.PositiveSmallIntegerField(default=0)

class Address(models.Model):
    address = models.CharField(max_length=100)
    roomOrFloor = models.CharField(max_length=100)
    buildingName = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    fee = models.OneToOneField(Fee, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    
class Contact(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(validators=[MinValueValidator(10000000)])


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(7)])
    hour_start = models.TimeField
    hour_end = models.TimeField