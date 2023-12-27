from django.contrib import admin
from .models import Menu, MenuCategory, Logger, Reservation


# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Logger)
admin.site.register(Reservation)
