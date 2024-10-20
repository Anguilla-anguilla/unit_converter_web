from django.urls import path
from . import views

app_name = 'unit'

urlpatterns = [
    path('length/', views.length, name='length'),
    path('weight/', views.weight, name='weight'),
    path('temperature/', views.temperature, name='temperature'),
]
