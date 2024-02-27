from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):

    class Meta:
        abstract = True



    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    



class Location(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tourist(User):
    passport_id = models.IntegerField()
    preferences = models.ForeignKey(Tour, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    user = models.OneToOneField(Tourist, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' review'


