from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from products.models import Product
from utils.generate_code import generate_code
from django.contrib.auth.models import User
from django.db.models.aggregates import Sum, Count

# Create your models here.


STATUS_CHOICES = (
    ('Inprogress', 'Inprogress'),
    ('Completed', 'Completed'),
)

class CartOrder(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"),related_name='user_cart', on_delete=models.SET_NULL, null=True, blank=True)
    code = models.CharField(_("Code"), default=generate_code, max_length=8,)
    order_status = models.CharField(_("Order Status"), max_length=10, choices=STATUS_CHOICES)

    def get_total(self):
        total = 0
        cart_details = self.cart_detail.all()
        for product in cart_details:
            total += product.total
        return total

    def get_total_items(self):
        total_items = self.cart_detail.aggregate(mytotal=Count('product'))
        return total_items
        
    def __str__(self):
        return self.code
    


class CartDetail(models.Model):
    order = models.ForeignKey(CartOrder, verbose_name=_("Order"), related_name='cart_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='cart_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.FloatField(_("Quantity"),default=0)
    price = models.FloatField(_("Price"),default=0)
    total = models.FloatField(_("Total"),default=0)
    def __str__(self):
        return str(self.order)




STATUS_CHOICES = (
    ('Recieved', 'Recieved'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
)

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"),related_name='user_orders', on_delete=models.SET_NULL, null=True, blank=True)
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