from django.db import models

class DataPoint(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
