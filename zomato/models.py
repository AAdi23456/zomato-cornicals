from django.db import models

class dish(models.Model):
   
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability=models.BooleanField(default=True)

class orders(models.Model):
    CostumerName=models.CharField(max_length=255)
    dish = models.CharField(max_length=255)
    status=models.CharField(max_length=25)

