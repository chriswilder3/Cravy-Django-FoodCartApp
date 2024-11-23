from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to Cravy")

def item(request):
    return HttpResponse('Items')
