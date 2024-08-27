from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductImages, Review, Category, Brand
from django.db.models import Count, Q
# Create your views here.


def product_list(request):
   #(1) conditions: price__gt=20 || price__lt=20 || price__range=(20,50) ||
   #    category=4 || category__name='Angela Hayes' || category__id__gt=10 ||
   #    name__contains='fox' || name__startswith='amy' || desc__isnull=True ||
   #(2) 2-conditions (AND) -> filter(price__gt=40, name__contains='fox')
   #    2-conditions (OR) -> filter(Q(price__gt=40) | Q(name__contains='fox'))   ( you can use | or & )
   #    ~Q(...): for(NOT)
   queryset = Product.objects.filter(Q(price__lt=20) | Q(name__contains='fox'))
   return render(request,'products/list.html',{'data': queryset })


# @@ django call it lazy queryset: @@ #
# queryset = Product.objects.all()                              --select all from Product
# queryset.filter(price__lt=20).filter(name__contains='fox')    --where conditions...
# django now excute it as ( SELECT * FROM Product WHERE (price > 20) AND (name LIKE '%fox%') )

# @@ compare between 2 fields value in the same table @@ #
# from django.db.models import F
# queryset = Product.objects.filter(id=F('price'))
# OR queryset = Product.objects.filter(id=F('category__id'))

# @@ Ordering data view @@ #
# queryset = Product.objects.order_by('name', ...) # Or '-name' == -> order_by('name').reverse()
# queryset = Product.objects.order_by('name')[:5] -> first 5 items
# queryset = Product.objects.order_by('name')[10:20] -> second 10 items
# earliest() - latest()

## @@ Return spesific column & join @@ #
# queryset = Product.objects.valuse('id','name','category__name')       values() / values_list()    .distinct() to remove tekrar
# queryset = Product.objects.defer('id')    as exclude() -> return all except 'id' for ex.

# for 1:1 OR 1:M relation ==>> select_related()   -   for M:M ==>> prefetch_related() 
# queryset = Product.objects.select_related('category').select_related('brand').all()  foriegn-keys >> join with 'Category' and 'Brand' tables


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
    

class BrandDetail(DetailView):
    model = Brand

    # filter products accordding to specific brand
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand = brand) 
        return context
