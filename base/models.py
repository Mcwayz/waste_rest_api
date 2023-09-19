from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

from django.db import models


# Waste Type Model
class Waste(models.Model):
    waste_id = models.AutoField(primary_key=True)
    waste_type = models.TextField(max_length=100)
    waste_desc = models.TextField(max_length=500)
    collection_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))


# User Profile Model
class UserProfile(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(max_length=200)
    user_id = models.AutoField(primary_key=True)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)


# Collections Model
class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    collection_date  = models.DateTimeField(blank=True)
    request = models.ForeignKey(User, on_delete=models.CASCADE)
    collector = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    collection_price =  models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))
    
    
# User Requests Model
class Requests(models.Model):
    request_id = models.AutoField(primary_key=True)
    number_of_bags =models.TextField(max_length=200)
    request_status  = models.DateTimeField(blank=True)
    waste = models.ForeignKey(Waste, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    request_date  = models.DateTimeField(default=timezone.now, blank=True)
    collection_price =  models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))
    
    
# Collectors (Driver) Model
class Collectors(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    vehicle = models.TextField(max_length=200)
    work_area = models.TextField(max_length=200)
    collector_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
# Driver Ratings Model  
class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating_score = models.TextField(max_length=200)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    