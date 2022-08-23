from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Choice(models.Model):
    city = models.CharField(max_length=64)
    duration = models.IntegerField()
    checkin = models.DateField(null=True, blank=True)
    checkout = models.DateField(null=True, blank=True)


class MyHotels(models.Model):
    hotelname = models.CharField(max_length=64, null=True, blank=True)
    type = models.CharField(max_length=64, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    rooms = models.IntegerField(null=True, blank=True)


class Booking(models.Model):
    hotelname = models.CharField(max_length=64, null=True, blank=True)
    type = models.CharField(max_length=64, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)