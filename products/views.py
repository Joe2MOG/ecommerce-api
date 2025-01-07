from django.shortcuts import render

# views.py
from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from .models import Category
from .serializers import CategorySerializer

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can create

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Associate the product with the authenticated user
 
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this endpoint

    def get_queryset(self):
        # Optionally filter to return only products created by the authenticated user
        return Product.objects.filter(user=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update or delete

class ProductSearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination  # Add pagination to the search results

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)

        if name:
            queryset = queryset.filter(name__icontains=name)  # Case-insensitive partial match on name
        if category:
            queryset = queryset.filter(category__name__icontains=category)  # Assuming category is a related model

        return queryset

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer