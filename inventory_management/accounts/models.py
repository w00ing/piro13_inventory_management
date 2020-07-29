from django.db import models
from phone_field import PhoneField


class Account(models.Model):

    """ Customer Model Definition """

    name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=140)

