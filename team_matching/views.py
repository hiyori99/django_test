from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request):
#   return HttpResponse("Hello")

def index(request):
  return render(request, "hello/index.html")

def brian(request):
  return  HttpResponse("Hello, Brian")

# def greet(request, name):
#   return HttpResponse(f"Hello, {name.capitalize()}!") #名前の先頭を大文字にする

def greet(request, name):
  return render(request, "hello/greet.html", {
    "name": name.capitalize() 
  }) #名前の先頭を大文字にする
