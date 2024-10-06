from rest_framework import generics
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer, BrandSerializerDetail, CategorySerializerDetail, ReviewSerializer, ProductSerializerDetail
from .models import Product, Category, Brand, Review
from .pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.permissions import IsAuthenticated


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    permission_classes = [IsAuthenticated]

class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerDetail


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
