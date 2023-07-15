from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

from django.db import models


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    longitude = models.TextField(max_length=200)
    latitude = models.TextField(max_length=200)


class Waste(models.Model):
    waste_id = models.AutoField(primary_key=True)
    waste_type = models.TextField(max_length=100)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))
    waste_desc = models.TextField(max_length=500)


class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    request_date  = models.DateTimeField(default=timezone.now, blank=True)
    user_collect_date  = models.DateTimeField(blank=True)
    is_collected = models.BooleanField(default=False)
    collection_date  = models.DateTimeField(blank=True)


class Subscription(models.Model):
    sub_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    waste = models.ForeignKey(Waste, on_delete=models.CASCADE)
    sub_date = models.DateTimeField(default=timezone.now, blank=True)
    
    
class Collectors(models.Model):
    collector_id = models.AutoField(primary_key=True)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.TextField(max_length=200)
    work_area = models.TextField(max_length=200)
    
    
class TaskAssignment(models.Model):
    task_id = models.AutoField(primary_key=True)
    collector = models.ForeignKey(Collectors, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    assigned_date  = models.DateTimeField(default=timezone.now, blank=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    