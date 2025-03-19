from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .api import RegisterView,LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]