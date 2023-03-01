from django.urls import path
from . import views

urlpatterns = [
    path('new_puppy/', views.new_puppy, name="new_puppy"),
]