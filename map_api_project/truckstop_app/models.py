from django.db import models


class Truckstop(models.Model):
    opis_id = models.IntegerField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    rack_id = models.IntegerField()
    retail_price = models.FloatField()

    class Meta:
        app_label = 'truckstop_app'

    def __str__(self):
        return self.name