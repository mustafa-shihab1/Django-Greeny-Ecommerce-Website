from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, BrandList, BrandDetail, product_list, CategoryDetail, add_to_favourites
from .api import product_list_api, ProductListAPI

app_name = 'products'

urlpatterns = [
    path('',ProductList.as_view(),name='product_list'),
    path('add_to_wish/', add_to_favourites, name='add_to_favourites'),
    path('test',product_list),
    path('<slug:slug>',ProductDetail.as_view(),name='product_detail'),
    path('category/',CategoryList.as_view(),name='category_list'),
    path('brand/',BrandList.as_view(),name='brand_list'),
    path('category/<slug:slug>',CategoryDetail.as_view(),name='category_detail'),
    path('brand/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),


    #api
    path('api/list', product_list_api),
    path('api/list/cbv', ProductListAPI.as_view()),

]