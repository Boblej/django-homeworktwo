from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'blog.html')

def state(request):
    return render(request,'state.html')