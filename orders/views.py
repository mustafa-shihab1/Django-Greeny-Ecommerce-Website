from django.shortcuts import render
from .models import Order, OrderDetail
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'orders/order_list.html',{'orders':orders})