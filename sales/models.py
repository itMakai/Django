from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField( max_digits=6, decimal_places=2)
    in_stock = models.IntegerField()


    def __str__(self) -> str:
        return f'{self.name} ({self.price})'
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
        
    def __str__(self) -> str:
        return f'{self.name} ({self.phone})'

class order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    in_stock = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.product} ({self.customer}) {self.order_date}'
    
    def total(self):
        return self.product.price * self.quantity


class orderDetail(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    Product = models.ForeignKey(Products, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.order} ({self.quantity})'
    
    def total(self):
        return self.unit_price * self.quantity