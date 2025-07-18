# innovation/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'innovation/index.html')