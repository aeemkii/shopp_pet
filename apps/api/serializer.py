from apps.shop.models import Product, Category, CheckOut

from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = "__all__"