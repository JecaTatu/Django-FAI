from .views import ProfileView, LogoutView, LoginView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path("user/<int:pk>", ProfileView.as_view(), name="profile")
]

