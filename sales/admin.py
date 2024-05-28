from django.contrib import admin
from sales.models import Products, Customer, order, orderDetail


# Register your models here.
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(order)
admin.site.register(orderDetail)