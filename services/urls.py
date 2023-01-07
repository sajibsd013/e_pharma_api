from django.urls import path, include
from rest_framework import routers
from .views import MobileDiagnostic, MobileDiagnosticDetails, Medicine, MedicineDetails
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
# Routers provide an easy way of automatically determining the URL conf.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('diagnostic/', MobileDiagnostic),
    path('diagnostic/<int:pk>/', MobileDiagnosticDetails),
    path('medicine/', Medicine),
    path('medicine/<int:pk>/', MedicineDetails),
]
