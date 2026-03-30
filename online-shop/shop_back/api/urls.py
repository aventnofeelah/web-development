from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('products/<int:id>/', views.ProductDetail.as_view()),

    path('categories/', views.CategoriesList.as_view()),
    path('categories/<int:id>/', views.CategoryDetail.as_view()),
    path('categories/<int:id>/products/', views.CategoryProducts.as_view()),
]