from rest_framework import generics
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer, BrandSerializerDetail, CategorySerializerDetail
from .models import Product, Category, Brand


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPI(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerDetail


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializerDetail
