from django.urls import path, include
from rest_framework import routers
from .views import DoctorAppointment, DoctorsAppointmentDetail, HomeMedicine, HomeMedicineDetails
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
# Routers provide an easy way of automatically determining the URL conf.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('medicine/', HomeMedicine),
    path('medicine/<int:pk>/', HomeMedicineDetails),
    path('doctor/', DoctorAppointment),
    path('doctor/<int:pk>/', DoctorsAppointmentDetail),
]
