from django.urls import path
from .views import *
from api import views
# Routers provide an easy way of automatically determining the URL conf.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('doctor/', DoctorAppointment),
    path('doctor/<int:pk>/', DoctorsAppointmentDetail),
]
