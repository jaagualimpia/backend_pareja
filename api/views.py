from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def order(request):
    


    return JsonResponse({'foo':'bar'})

def product(request):
    return JsonResponse({'foo':'bar'})

def order(request):
    return JsonResponse({'foo':'bar'})