from django.urls import path
from . import views

urlpatterns = [
    path('api/products/<int:pk>/', views.product_detail),
]