from django.db import models

from django.contrib.auth.models import User

class Artist(models.Model):
    ShowID = models.ForeignKey(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=100)
    MiddleName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)


class Arena(models.Model):
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)


class Show(models.Model):
    ArenaID = models.ForeignKey(User, on_delete=models.CASCADE)
    SoldTicketsOverall = models.IntegerField()
    Date = models.DateTimeField()

class Ticket(models.Model):
    ShowID = models.ForeignKey(User, on_delete=models.CASCADE)
    Cost = models.FloatField()
    Place = models.IntegerField()

class Visitor(models.Model):
    TicketID = models.ForeignKey(User, on_delete=models.CASCADE)
    MiddleName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)