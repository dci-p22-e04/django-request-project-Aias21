from django.db import models


class ExchangeRate(models.Model):
    currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=20, decimal_places=4)
    date = models.DateField()
