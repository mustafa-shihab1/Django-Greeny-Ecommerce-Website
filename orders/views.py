from django.shortcuts import render
from .models import Order, OrderDetail

# Create your views here.

def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'orders/order_list.html',{'orders':orders})