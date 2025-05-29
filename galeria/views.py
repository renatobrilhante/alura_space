from django.shortcuts import render
from django.http import HttpResponse

def index(request): # receber a requisição
    return HttpResponse('<h1>Alura Space</h1>')