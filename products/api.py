from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product

# Function:
@api_view(['GET'])                                          # ---> determine method
def product_list_api(request):
    products = Product.objects.all()                        # ---> python-list
    data = ProductSerializer(products, many=True).data      # ---> convert python-list to json
    return Response({'Success':True, 'Product-List':data})  # ---> return json


# Generic Views ---> Class Based Views:
## list and create
class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

## retrieve, update and delete
class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Class Based Views:
class ProductDetailAPi(generics.GenericAPIView):
    queryset = Product
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        data = ProductSerializer(product).data
        return Response(data)

    def patch(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response({"Success":True})