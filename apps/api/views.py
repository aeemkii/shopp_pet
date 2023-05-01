from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# from rest_framework.generics import ListAPIView
from apps.api.serializer import ProductSerializer, CategorySerializer, CheckOutSerializer
from apps.shop.models import Product, Category, CheckOut

class ProductListAPIView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_available=True)
    permission_classes = [IsAuthenticated]


class CategoryListAPIView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

class CheckOutAPIView(viewsets.ModelViewSet):
    serializer_class = CheckOutSerializer
    queryset = CheckOut.objects.all()
    permission_classes = [IsAuthenticated]