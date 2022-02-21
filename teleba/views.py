from django.shortcuts import render
from numpy import require

def home_view(request):
    return render(request,'teleba/home.html')


def detail_view(request):
    return render(request,'teleba/single.html') 

