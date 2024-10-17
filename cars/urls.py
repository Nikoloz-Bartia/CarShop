from django.urls import path , include
from .views import *




urlpatterns = [
    path('', cars, name='cars'),
    path('cars/<int:pk>', pk_cars, name='pk_cars'),
    path('add/', add_car, name='add_car'),
]