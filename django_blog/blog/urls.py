from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('', include('django.contrib.auth.urls')),
]

