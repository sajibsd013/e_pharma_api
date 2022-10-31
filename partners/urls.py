from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from partners import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'doctors', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('nurse-regi/', views.nurse_regi),
    path('caregiver-regi/', views.care_giver),
    path('physiotherapist-regi/', views.physiotherapist),
    path('partner-regi/', views.partner),
    # path('doctor-regi/', views.doctor),
    path('doctor-regi/', views.DoctotList.as_view()),
    path('dmf-doctor-regi/', views.dmf_doctor),
    path('', include(router.urls)),
]
