from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductImages, Review, Category, Brand
from django.db.models import Count
# Create your views here.


class ProductList(ListView):
    model = Product
    # show 5 product for each page
    paginate_by = 1


class ProductDetail(DetailView):
    model = Product

# get product images 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = ProductImages.objects.filter(product=self.get_object())
        context["reviews"] = Review.objects.filter(product=self.get_object())
        return context
    

class CategoryList(ListView):
    model = Category
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(product_count=Count('product_category') )
        return context

class BrandList(ListView):
    model = Brand
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all().annotate(product_count=Count('product_brand') )
        return context
