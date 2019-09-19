from django.urls import path
from django.contrib.auth import views as auth_views
from account import views as account_views

from . import views

app_name = 'account'

urlpatterns = [
    path('registrar/', account_views.register, name='registrar'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),
]