from django.urls import path

from . import views
from .views import HelloWorldView

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('add-dish/', views.add_dish, name='add_dish'),
    path('hello/', HelloWorldView.as_view(), name='hello'),
]