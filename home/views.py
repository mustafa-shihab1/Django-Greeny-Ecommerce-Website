from django.shortcuts import render
from products.models import Category, Product, Brand
from django.db.models.aggregates import Count

# Create your views here.

def home(request):
    categories = Category.objects.all().annotate(product_count=Count('product_category'))
    featured_products = Product.objects.filter(flag = 'Feature').order_by('?')[:6]
    new_products = Product.objects.filter(flag = 'New').order_by('?')[:12]
    brands = Brand.objects.all().annotate(product_count=Count('product_brand')).order_by('?')[:12]
    return render(request,'home/home.html',{
        'categories':categories,
        'featured_products':featured_products,
        'new_products':new_products,
        'brands':brands,
        })
