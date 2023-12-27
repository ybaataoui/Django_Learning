from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    reservation_day = models.CharField(max_length=200)
    seats = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Vehicule(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default='Vehicule')
