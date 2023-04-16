from django.db import models

# Create your models here.
class Forecast(models.Model):
    name = models.CharField(max_length=12)
    data = models.DateField
    description = models.TextField()
    lucky_number = models.PositiveIntegerField()
    color = models.TextField()