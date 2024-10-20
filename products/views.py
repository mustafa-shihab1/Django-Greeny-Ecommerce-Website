from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse

from accounts.models import Profile
from .models import Product, ProductImages, Review, Category, Brand
from django.db.models import F, Q, Func, Value, CharField
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from django.db.models.functions import Concat
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm


# Create your views here.

class ProductList(ListView):
    model = Product
    # show 5 product for each page
    paginate_by = 50


class ProductDetail(DetailView):
    model = Product

# get product images 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # (for cbv) self.get_object() -> this return the current openned item
        context["images"] = ProductImages.objects.filter(product=self.get_object()) 
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(category=self.get_object().category)[0:10]
        return context
    

class CategoryList(ListView):
    model = Category
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(product_count=Count('product_category') )
        return context


class CategoryDetail(DetailView):
    model = Category


class BrandList(ListView):
    model = Brand
    paginate_by = 10

    def get_queryset(self):
        queryset = super(BrandList, self).get_queryset()
        queryset = Brand.objects.all().annotate(product_count=Count('product_brand') )
        return queryset
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["brands"] = Brand.objects.all().annotate(product_count=Count('product_brand') )
    #     return context
    

class BrandDetail(DetailView):
    model = Brand

    # filter products accordding to specific brand
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand = brand) 
        return context



def product_list(request):
    queryset = Product.objects.price_greater_than(30)    # queryset cache (good performance)
    print(queryset)    
    return render(request,'products/list.html',{'data': queryset })



@login_required
def add_review(request, slug):
    product = Product.objects.get(slug = slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.product = product
            myform.save()

            return redirect(reverse('products:product_detail', kwargs={'slug':slug}))



@login_required
def add_to_favourites(request):
    product = Product.objects.get(id=request.POST['productid'])
    profile = Profile.objects.get(user=request.user)

    if product in profile.favourites.all():
        profile.favourites.remove(product)
    else:
        profile.favourites.add(product)
