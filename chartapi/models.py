from django.db import models

class Chart(models.Model):
    time = models.TimeField(True)
    closing_price = models.CharField(max_length=30)
