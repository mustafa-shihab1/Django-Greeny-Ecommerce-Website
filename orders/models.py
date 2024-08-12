from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from products.models import Product
from utils.generate_code import generate_code

# Create your models here.


STATUS_CHOICES = (
    ('Recieved', 'Recieved'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
)

class Order(models.Model):
    code = models.CharField(_("Code"), default=generate_code, max_length=8,)
    order_status = models.CharField(_("Order Status"), max_length=10, choices=STATUS_CHOICES)
    order_time = models.DateTimeField(_("Order Time"), default=timezone.now)
    delivery_time = models.DateTimeField(_("Delivery Time"),null=True, blank=True)
    def __str__(self):
        return self.code


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Order"), related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='order_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.FloatField(_("Quantity"),)
    price = models.FloatField(_("Price"))
    def __str__(self):
        return str(self.order)