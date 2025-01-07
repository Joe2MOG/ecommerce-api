from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    # Use a string representation for category
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),  # Queryset to match category
        slug_field='name'  # Use the 'name' field of Category as the slug
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_date']
        read_only_fields = ['id', 'created_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Include only the fields needed