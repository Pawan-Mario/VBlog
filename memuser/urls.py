from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    # path('members/',include('django.contrib.auth.urls')),
    # path('members/',include('memuser.urls')),
    path('register/',UserRegisterView.as_view(),name='register'),
]