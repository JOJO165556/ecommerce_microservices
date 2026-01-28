from django.urls import path
from orders.views import create_order

urlpatterns = [
    path('api/orders/create/', create_order),
]