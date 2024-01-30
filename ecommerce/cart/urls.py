from django.urls import path
from .views import AddToCartView, ViewCartView, UpdateCartView

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('view-cart/', ViewCartView.as_view(), name='view_cart'),
    path('update-cart-item/<int:pk>/', UpdateCartView.as_view(), name='update_cart_item'),
]