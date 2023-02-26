from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.crud, name='crud'),
    path('login/', views.login, name='login'),
]