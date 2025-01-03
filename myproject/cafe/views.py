from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .forms import DishForm
from .models import Dish
from .serializers import DishSerializer


# Create your views here.

def index(request):
    return render(request, 'cafe/index.html')

def menu(request):
    categories = Dish.CATEGORY_CHOICES
    dishes_by_category = {category[1]: Dish.objects.filter(category=category[0], is_available=True) for category in categories}
    return render(request, 'cafe/menu.html', {'dishes_by_category': dishes_by_category})

def about(request):
    return HttpResponse("Информация о нашем кафе")

def add_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = DishForm()
    return render(request, 'cafe/add_dish.html', {'form': form})

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"})

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})

class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
