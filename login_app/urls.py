from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='home'),
    path('registration/', views.registration, name='registration'),
    path('message/', views.message, name='message'),
]