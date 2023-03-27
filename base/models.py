from django.db import models
from decimal import Decimal
from django.utils import timezone
# Create your models here.

from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.TextField(max_length=40)
    firstname = models.TextField(max_length=60)
    lastname = models.TextField(max_length=60)
    address = models.TextField(max_length=200)
    longitude = models.TextField(max_length=200)
    latitude = models.TextField(max_length=200)


class Waste(models.Model):
    waste_id = models.AutoField(primary_key=True)
    waste_type = models.TextField(max_length=100)
    waste_desc = models.TextField(max_length=500)


class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    collection_date  = models.DateField()
    collect = models.BooleanField(default=False)
    remarks = models.CharField(max_length=300)


class Subscription(models.Model):
    sub_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    waste_id = models.ForeignKey(Waste, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))
    sub_date = models.DateTimeField(default=timezone.now, blank=True)