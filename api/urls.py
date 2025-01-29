from django.urls import path
from . import views

urlpatterns = [
    path("product/", views.ProductListCreate.as_view(), name="ProductListCreate"),
    path("product/<int:pk>/", views.ProductDetailUpdateDelete.as_view(), name="ProductRetrieveUpdateDestroy"),

    path("brand/", views.BrandListCreate.as_view(), name="BrandListCreate"),
    path("brand/<int:pk>/", views.BrandDetailUpdateDelete.as_view(), name="BrandDetailUpdateDelete"),
    
    path("category/", views.CategoryListCreate.as_view(), name="CategoryListCreate"),
    path("category/<int:pk>/", views.CategoryDetailUpdateDelete.as_view(), name="CategoryDetailUpdateDelete"),
]
