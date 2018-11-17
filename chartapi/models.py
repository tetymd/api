from django.db import models

class Stock_9432(models.Model):
    time = models.CharField(max_length=30)
    opening_price = models.CharField(max_length=30)
    high_price = models.CharField(max_length=30)
    low_price = models.CharField(max_length=30)
    closing_price = models.CharField(max_length=30)
    volume = models.CharField(max_length=30)
    ad_closing_price = models.CharField(max_length=30)
