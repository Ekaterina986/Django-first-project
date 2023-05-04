from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)


class  Measurement (models.Model):
    temperature = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateField(auto_now=True)