from django.urls import path
from rest_framework import routers
from partners import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'doctors', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('nurse/', views.nurse),
    path('caregiver/', views.caregiver),
    path('physiotherapist/', views.physiotherapist),
    path('pharmacy/', views.pharmacy),
    # path('doctor-regi/', views.doctor),
    path('doctor/', views.DoctotList.as_view()),
    path('doctor/<int:pk>', views.doctor_details),
    path('dmf-doctor/', views.dmf_doctor),
    # path('', include(router.urls)),
]
