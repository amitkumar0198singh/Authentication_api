from django.urls import path
from api import views


# Create your urls here.

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('refresh-token/', views.RefreshTokenView.as_view(), name='refresh'),
]
