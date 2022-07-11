from django.shortcuts import render
from django.http import HTTPResponse

def home(request):
    return HTTPResponse("Hey beautiful")