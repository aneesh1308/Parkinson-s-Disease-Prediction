from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mri/', views.mriForm, name='mri'),
    path('voice/', views.voice, name='voice'),
    path('spiral', views.spiral, name='spiral')
]