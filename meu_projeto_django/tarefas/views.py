from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ola_django(request):
    return HttpResponse("ola, mundo")