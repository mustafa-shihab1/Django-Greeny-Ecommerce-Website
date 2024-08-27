from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, BrandList, BrandDetail, product_list

app_name = 'products'

urlpatterns = [
    path('',ProductList.as_view(),name='product_list'),
    path('test',product_list),
    path('<slug:slug>',ProductDetail.as_view(),name='product_detail'),
    path('category/',CategoryList.as_view(),name='category_list'),
    path('brand/',BrandList.as_view(),name='brand_list'),
    path('brand/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),

]