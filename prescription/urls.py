from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('data/', views.get_prescription_data),
    path('pres/', views.prescriptions),
    path('pres/<int:pk>', views.prescriptions_detail),
    path('doctor/', views.doctor_info),
    path('doctor/<int:pk>', views.doctor_info_detail),
]
