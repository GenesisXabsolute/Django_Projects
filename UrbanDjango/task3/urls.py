from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index1, name='index1'),
    path('games/', views.index2, name='index2'),
    path('basket/', views.index3, name='index3'),
]