from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product


@api_view(['GET'])                                          # ---> determine method
def product_list_api(request):
    products = Product.objects.all()                        # ---> python-list
    data = ProductSerializer(products, many=True).data      # ---> convert python-list to json
    return Response({'Success':True, 'Product-List':data})  # ---> return json



class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetialAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer