from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    context = {
        "name":"Raselacademy"
        }
    return render(request, 'hello_world/index.html', context)
