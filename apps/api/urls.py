
from django.urls import path, include
from rest_framework import routers
from .views import ProductListAPIView, CategoryListAPIView, CheckOutAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
    

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Shopp",
        default_version='v1',
        description="Shop api",
        contact=openapi.Contact(email="limkengha@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register('products', ProductListAPIView)
router.register('categories', CategoryListAPIView)
router.register('checkout', CheckOutAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui("swagger")),    
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]