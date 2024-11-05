from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import Group


# Create your models here.

# Creation de la table réservation

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.booking_date.strftime('%Y-%m-%d %H:%M')}"


# Creation de la table réservation
class Menu(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.price} GNF "

