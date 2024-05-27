from django.db import models

# Create your models here.

class products (models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField( max_digits=6, decimal_places=2)
    in_stock = models.IntegerField()


    def __str__(self) -> str:
        return f'{self.name} ({self.price})'
