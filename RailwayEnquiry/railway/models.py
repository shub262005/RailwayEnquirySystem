from django.db import models
from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime

# Create your models here.


from django.db import models


class Train(models.Model):
    train_number = models.CharField(max_length=10, primary_key=True)
    departure_station = models.CharField(max_length=100)
    arrival_station = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return self.train_number


class Passenger(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=10)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return self.ticket_number
