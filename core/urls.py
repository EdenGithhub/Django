from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('about/', views.about, name='about'),
    path('submit/', views.submit_culture, name='submit_culture'),
]
