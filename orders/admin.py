from django.contrib import admin
from .models import Order, OrderDetail, CartOrder, CartDetail

# Register your models here.


admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(CartOrder)
admin.site.register(CartDetail)