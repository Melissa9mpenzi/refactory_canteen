from django.db import models
from django.utils import timezone
from datetime import datetime
#from forms import ProductForm

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField()#Cocacola
    price = models.FloatField() # i.e 3.99$
    description = models.TextField()#500ml bottle
    quantity = models.IntegerField()# 24 pieces
    category = models.CharField(max_length=255)# beverages, electronics, office appliances
    brand = models.CharField(max_length=255)

class Transaction(models.Model):
    amount = models.FloatField()
    tx_id = models.CharField(max_length=255)# it's like a receipt number
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #3, 6, 20, The foreign key defines what happens in case a product is deleted hence the need for an on_delete function
    name = models.CharField(max_length=255) # Melly
    phone = models.CharField(max_length=255) # 07001357891
    receiver = models.CharField(max_length=255, default='Refactory') #Dave
    date = models.DateTimeField(default=datetime.now()) # today
    method = models.CharField(max_length=255) #"Bank", "Cash", "VISA", "Mobile Money"