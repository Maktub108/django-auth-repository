from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(
        template_name='main/login.html',
        form_class=LoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]