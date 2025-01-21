from django.shortcuts import render

def index(request):
    return render(request, 'chat/templates/chat/index.html')