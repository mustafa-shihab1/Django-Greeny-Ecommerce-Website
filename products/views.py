from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductImages, Review
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
    