from django.urls import path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.blog_list),
    path('<int:pk>', views.blog_detail),
    path('comment', views.comment_list),
    path('comment/<int:pk>/', views.comment_detail),
]
