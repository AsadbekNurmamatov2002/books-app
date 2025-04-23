from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/logreg.html'), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]