from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import HelloWorldView, DishViewSet

router = DefaultRouter()
router.register('dishes', DishViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('add-dish/', views.add_dish, name='add_dish'),
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('', include(router.urls)),
]