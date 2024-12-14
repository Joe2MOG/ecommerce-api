from django.urls import path
from .views import ProductListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ProductListView, get_products

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/products/auth/', get_products, name='auth-product-list'),
]
