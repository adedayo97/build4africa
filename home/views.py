# home/views.py
from django.shortcuts import render, redirect

def home(request):
    if request.GET.get('refresh'):
        return redirect('home') 
    return render(request, 'home/home.html')