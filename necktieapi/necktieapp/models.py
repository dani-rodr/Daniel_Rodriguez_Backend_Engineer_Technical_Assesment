from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Fee(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    daysIncludingWesternMeds = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "${}, {} days inclusive of Western Medicine".format(self.price, self.daysIncludingWesternMeds)

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.street, self.city)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    fee = models.OneToOneField(Fee, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
class Contact(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='contacts')
    number = models.PositiveIntegerField(validators=[MinValueValidator(10000000)])

    def __str__(self):
        return "{}".format(self.number)
class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(7)])
    hour_start = models.TimeField
    hour_end = models.TimeField