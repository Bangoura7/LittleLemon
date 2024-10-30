from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

# Creation de la table réservation

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators= [MinValueValidator(1)])
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.booking_date.strftime('%Y-%m-%d %H:%M')}"

class Menu(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    inventory = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.title} - {self.price} GNF "

