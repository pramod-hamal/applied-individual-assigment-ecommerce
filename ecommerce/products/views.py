# views.py
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from .models import Product
from .serializers import ProductSerializer, CreateProductSerializer, UpdateProductSerializer
from api.mixins import VendorPermissionMixin
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

class ProductPublicList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryPublicList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category=category)

class ProductList(VendorPermissionMixin,ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.filter(added_by=self.request.user)


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = 'slug'
    serializer_class = ProductSerializer

class ProductCreate(VendorPermissionMixin,CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ProductUpdate(VendorPermissionMixin,RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer
    lookup_field = 'slug'
    def perform_update(self, serializer):
        if serializer.instance.added_by == self.request.user:
            serializer.save()
            serializer = ProductSerializer(serializer.instance)
            return Response(serializer.data)
        else:
            raise PermissionDenied("You cannot update this product")

class ProductDelete(VendorPermissionMixin,RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def perform_destroy(self, instance):
        if instance.added_by == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You cannot delete this product")    
