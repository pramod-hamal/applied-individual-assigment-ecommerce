from rest_framework import generics
from rest_framework.response import Response
from api.mixins import CustomerPermissionMixin
from .models import Product, CartItem, Cart
from .serializers import  CartItemSerializer, CartSerializer, UpdateCartItemSerializer

from rest_framework import status

class AddToCartView(CustomerPermissionMixin,generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_create(self, serializer, raise_exception=True):
        product_id = self.request.data.get('product')
        product = Product.objects.get(id=product_id)
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user, is_ordered=False)
        savedInstance = serializer.save(cart=cart, product=product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
class ViewCartView(CustomerPermissionMixin,generics.RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user, is_ordered=False)
        return cart
class UpdateCartView(CustomerPermissionMixin,generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_update(self, serializer):
        cartItem = serializer.instance
        cartItem.quantity = self.request.data.get('quantity')
        cartItem.save()

        updated_serializer = CartItemSerializer(cartItem)
        return Response(updated_serializer.data, status=status.HTTP_200_OK)
