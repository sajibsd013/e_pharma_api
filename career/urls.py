from django.urls import path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('job/', views.job_list),
    path('job/<int:pk>', views.job_detail),
]
