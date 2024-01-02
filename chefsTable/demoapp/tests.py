from django.test import TestCase
from datetime import datetime
from .models import Reservation

# Create your tests here.

class ReservationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.reservation = Reservation.objects.create(
            name = "Youssef Baataoui",
            contact = "407-955-5555",
            time = "11:58:00",
            count = 4,
            notes = "We would like a table outdoor."
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.name, str)
        self.assertIsInstance(self.reservation.contact, str)

    def test_timestamps(self):
        self.assertIsInstance(self.reservation.time, datetime)







  

