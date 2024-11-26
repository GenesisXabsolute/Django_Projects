from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.index1, name='index1'),
    path('class/', views.index2, name='index2'),
    path('', views.index3, name='index3')
]