from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from apps.api.serializer import ProductSerializer, CategorySerializer
from apps.shop.models import Product, Category

class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_available=True)


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()