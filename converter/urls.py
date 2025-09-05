from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temperature/', views.temperature, name='temperature'),
    path('weight/', views.weight, name='weight'),
    path('result/', views.result, name='result'),
]