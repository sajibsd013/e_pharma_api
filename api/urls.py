from django.urls import path, include
from rest_framework import routers
from .views import AppointmentViewSet, CallAppointmentViewSet, CallDoctorViewSet, DoctorViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'call-doctors', CallDoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'call-appointments', CallAppointmentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('services/', views.service_list),
    path('services/<int:pk>', views.services_detail),
    # path('doctors/', views.doctors_list),
    # path('doctors/<int:pk>', views.doctors_detail),
    # path('call-doctors/', views.call_doctors_list),
    # path('call-doctors/<int:pk>', views.call_doctors_detail),
    path('faqs/', views.faqs_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
