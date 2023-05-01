from django.urls import path
from apps.shop import views
urlpatterns = [
    path("product/list/", views.ProductListView.as_view(),), 
    path("detail/product/<int:pk>/", views.DetailProductView.as_view(),),
]