from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'work/index.html')

def youth(request):
    return render(request, "work/youth_empowerment.html")

def governance(request):
    return render(request, "work/good_governance.html")

def fintech(request):
    return render(request, "work/fintech_inclusion.html")

def education(request):
    return render(request, "work/education.html")


 

 