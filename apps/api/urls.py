from django.urls import path

from . import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Shop",
        default_version='v1',
        description="Shop api",
        contact=openapi.Contact(email="limkengha@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path("docs/", schema_view.with_ui("swagger")),
    path("products/", views.ProductListAPIView.as_view()), 
    path("categories/", views.CategoryListAPIView.as_view()),
    
]