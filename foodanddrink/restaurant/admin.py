from django.contrib import admin
from .models import Customer, Product, Category, Order, OrderDetail
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Category)
