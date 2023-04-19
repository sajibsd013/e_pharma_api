from django.urls import path, include
from api import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('guidelines/', views.guidelines_list),
    path('services/', views.service_list),
    path('services/<int:pk>', views.services_detail),
    path('faqs/', views.faqs_list),
    path('bmi-faqs/', views.bmi_faqs_list),
    path('speciality/', views.speciality_list),
    path('send-otp/', views.set_otp),
    path('send-sms', views.send_promotional_sms),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
