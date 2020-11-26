from .views import UserDetailAPIView
from django.urls import path, include

urlpatterns = [
    path('view', UserDetailAPIView.as_view())
]