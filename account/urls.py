from django.contrib.auth import views as auth_views
from django.urls import path

from .views import register

# from .views import user_login

app_name = 'account'
urlpatterns = [
    # url-адреси для входу та виходу
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
