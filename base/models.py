from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.models import User

# Waste Type Model
class Waste(models.Model):
    waste_id = models.AutoField(primary_key=True)
    waste_type = models.CharField(max_length=100)
    waste_desc = models.CharField(max_length=500)
    collection_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))

# User Profile Model
class CustomerProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(max_length=200)
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    
# Collectors (Driver) Model
class CollectorProfile(models.Model):
    collector_id = models.AutoField(primary_key=True)
    vehicle = models.CharField(max_length=200)
    work_area = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    

# Collections Model
class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    collection_date = models.DateTimeField()
    collection_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))
    request = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections_requested')
    collector = models.ForeignKey(CollectorProfile, on_delete=models.CASCADE, related_name='collections_collected')

# User Requests Model
class Requests(models.Model):
    request_id = models.AutoField(primary_key=True)
    number_of_bags = models.PositiveIntegerField()
    request_status = models.CharField(max_length=100)
    request_date = models.DateTimeField(default=timezone.now, blank=True)
    waste = models.ForeignKey(Waste, on_delete=models.CASCADE, related_name='requests')
    collection_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='user_requests')
    

# Driver Ratings Model
class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating_score = models.PositiveIntegerField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='ratings')
