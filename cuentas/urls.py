from django.urls import path
from . import views

urlpatterns = [
    path('', views.seguimiento, name='seguimiento'),
    path('addCategory/', views.seguimiento, name='seguimiento'),
    path('cuenta/<int:pk>/', views.detallesSeguimiento, name='detalles'),
]
