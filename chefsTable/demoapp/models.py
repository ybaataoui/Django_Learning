from unicodedata import name
from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menu(models.Model):
    name  = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")

    def __str__(self) -> str:
        return self.name

class Logger(models.Model): 
    first_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200) 
    time_log = models.TimeField()  

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank = True)
    

    def __str__(self) -> str:
        return self.name

