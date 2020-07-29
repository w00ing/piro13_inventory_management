from django.db import models
from phone_field import PhoneField


class Customer(models.Model):

    """ Customer Model Definition """

    name = models.CharField(max_length=25)
    phone_number = PhoneField()
    address = models.CharField(max_length=140)

