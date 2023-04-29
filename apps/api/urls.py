
from django.urls import path, include
from rest_framework import routers
from .views import ProductListAPIView, CategoryListAPIView

router = routers.DefaultRouter()
router.register('products', ProductListAPIView)
router.register('categories', CategoryListAPIView)

urlpatterns = [
    path('', include(router.urls)),
]