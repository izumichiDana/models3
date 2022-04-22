from django.db import models


class Order(models.Model):
    user = models.CharField(max_length=12)
    data = models.DateField()


class Admin(models.Model):
    name = models.CharField(max_length=10)