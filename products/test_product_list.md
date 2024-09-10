def product_list(request):
    queryset = Product.objects.price_greater_than(30)    # queryset cache (good performance)
    print(queryset)    
    return render(request,'products/list.html',{'data': queryset })

# (1) conditions: price__gt=20 || price__lt=20 || price__range=(20,50) ||
#    category=4 || category__name='Angela Hayes' || category__id__gt=10 ||
#    name__contains='fox' || name__startswith='amy' || desc__isnull=True ||
# (2) 2-conditions (AND) -> filter(price__gt=40, name__contains='fox')
#    2-conditions (OR) -> filter(Q(price__gt=40) | Q(name__contains='fox'))   ( you can use | or & )
#    ~Q(...): for(NOT)

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

# #######################################################################################

# aggregation functions => Count, Min, Max, Avg, Sum
# EX: queryset = Product.objects.aggregate(mySum=Sum('price'),myAvg=(Avg('price'))) ; print(queryset)  
# 
# ## @@ Annotation @@ #
# to create new field accordding to a specific operation without exist in db.
#
# Examples::
#
# Math-operation:
# queryset = Product.objects.annotate(price_tax=F('price')*0.8)  
# 
# Conctatination:
# queryset = Product.objects.annotate(
#   full_name = Concat(
#     'name','sku', output_field=CharField()
#     )
# ) 
#