from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='base/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='base/logout.html'), name="logout"),
    path('staff_view/',views.staff_view, name='staff_view'),
]