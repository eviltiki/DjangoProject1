from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import DishViewSet

router = DefaultRouter()
router.register('dishes', DishViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('add-dish/', views.add_dish, name='add_dish'),
    path('', include(router.urls)),
]