from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    stock = models.IntegerField()
    price_sell = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=50, blank=True)
    price_bought = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    brand = models.CharField(max_length=100)
    season = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.code} - {self.type}'