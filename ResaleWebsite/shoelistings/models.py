from django.db import models

class shoeListing(models.Model):
    name = models.CharField()
    retail = models.IntegerField()
    resale = models.IntegerField()
    profit = models.IntegerField()
    date = models.IntegerField()
