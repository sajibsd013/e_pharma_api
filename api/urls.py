from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('services/', views.service_list),
    path('services/<int:pk>', views.services_detail),
    path('faqs/', views.faqs_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
