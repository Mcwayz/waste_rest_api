from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# User Profile Model


class CustomerProfile(models.Model):
    customer_id = models.AutoField(primary_key=True)
    address = models.TextField(max_length=200)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)


# Waste Type Model


class Waste(models.Model):
    waste_id = models.AutoField(primary_key=True)
    waste_type = models.CharField(max_length=100)
    waste_desc = models.CharField(max_length=500)
    collection_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))
    
    
# Collectors (Driver) Model


class CollectorProfile(models.Model):
    collector_id = models.AutoField(primary_key=True)
    vehicle = models.CharField(max_length=200)
    work_area = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    waste = models.ForeignKey(Waste, on_delete=models.CASCADE, related_name='collector_wastes')


# User Requests Model


class Requests(models.Model):
    request_id = models.AutoField(primary_key=True)
    location = models.TextField(max_length=254)
    number_of_bags = models.PositiveIntegerField()
    request_status = models.CharField(max_length=100)
    request_date = models.DateTimeField(default=timezone.now, blank=True)
    waste = models.ForeignKey(Waste, on_delete=models.CASCADE, related_name='requests')
    collection_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.0))
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='user_requests')


# Collections  Model


class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    collection_date = models.DateTimeField(default=timezone.now, blank=True)
    request = models.ForeignKey(Requests, on_delete=models.CASCADE, related_name='collections_requested')
    collector = models.ForeignKey(CollectorProfile, on_delete=models.CASCADE, related_name='collections_collected')


# Driver Ratings Model


class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating_score = models.PositiveIntegerField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='ratings')



# Wallet Model 


class Wallet(models.Model):
    wallet_id = models.AutoField(primary_key=True)
    balance = models.DecimalField(max_digits=65, decimal_places=2, default=Decimal(0.0))
    collector = models.OneToOneField(CollectorProfile, on_delete=models.CASCADE)
    
    
# Wallet History


class WalletHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    transaction_type =  models.CharField(max_length=100)
    transaction_date = models.DateTimeField(default=timezone.now, blank=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='wallet_history')
    old_wallet_balance = models.DecimalField(max_digits=65, decimal_places=2, default=Decimal(0.0))
    new_wallet_balance = models.DecimalField(max_digits=65, decimal_places=2, default=Decimal(0.0))
    transaction_amount = models.DecimalField(max_digits=65, decimal_places=2, default=Decimal(0.0))
    
    
# Commission Model


class CommissionCollector(models.Model):
    txn_id = models.AutoField(primary_key=True)
    collector = models.OneToOneField(CollectorProfile, on_delete=models.CASCADE)
    comission_settlement_date = models.DateTimeField(default=timezone.now, blank=True)
    comission =  models.DecimalField(max_digits=65, decimal_places=2, default=Decimal(0.0))


# Waste General Legder Wallet  
    
    
class WasteGL(models.Model):
    TRANSACTION_TYPES = (
        ('DEPOSIT', 'Deposit'),
        ('TRANSFER', 'Transfer'),
    )
    gl_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_TYPES)
    comission_settlement_date = models.DateTimeField(default=timezone.now, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='ledger')
    service_charge =  models.DecimalField(max_digits=65, decimal_places=2, default=Decimal(0.0))
    old_GL_balance = models.DecimalField(max_digits=65, decimal_places=2, default=Decimal(0.0))
    new_GL_balance = models.DecimalField(max_digits=65, decimal_places=2, default=Decimal(0.0))
    extras = models.CharField(max_length=100, default="None")

     