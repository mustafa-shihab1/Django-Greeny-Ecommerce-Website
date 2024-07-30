from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.


class ProductList(ListView):
    model = Product
    # show 5 product for each page
    paginate_by = 1


class ProductDetail(DetailView):
    model = Product

