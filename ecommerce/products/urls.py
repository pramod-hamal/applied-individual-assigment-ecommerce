from django.urls import path
from .views import ProductCategoryPublicList,ProductPublicList,ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    path('', ProductPublicList.as_view(), name='product-public-list'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path("category/<str:category>/", ProductCategoryPublicList.as_view(), name="product-category"),
    path('vendor/products/', ProductList.as_view(), name='product-list'),
    path('vendor/products/create/', ProductCreate.as_view(), name='product-create'),
    path('vendor/products/<slug:slug>/update/', ProductUpdate.as_view(), name='product-update'),
    path('vendor/products/<slug:slug>/delete/', ProductDelete.as_view(), name='product-delete'),
]