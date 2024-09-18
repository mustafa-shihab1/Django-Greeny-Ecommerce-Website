from django.shortcuts import render
from .models import Order, OrderDetail, CartOrder, CartDetail
from products.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'orders/order_list.html',{'orders':orders})


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['productid']
        quantity = request.POST['quantity']

        product = Product.objects.get(id=product_id)
        cart = CartOrder.objects.get(user=request.user, order_status='Inprogress')
        cart_detail, created = CartDetail.objects.get_or_create(
            order = cart,
            product = product
        )
        cart_detail.quantity = int(quantity)
        cart_detail.price = product.price
        cart_detail.total = int(quantity) * product.price
        cart_detail.save()
        