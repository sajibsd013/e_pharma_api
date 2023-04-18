from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import product_list, Orders, OrdersDetails, medicine_list

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('orders/', Orders),
    path('orders/<int:pk>', OrdersDetails),
    path('product/', product_list),
    path('medicine/', medicine_list),
]
