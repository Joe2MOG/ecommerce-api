from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductSearchView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#from .views import ProductListView, get_products

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),  # GET
    path('create/', ProductCreateView.as_view(), name='product-create'),  # POST
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('search/', ProductSearchView.as_view(), name='product-search'),  # search URL
]

