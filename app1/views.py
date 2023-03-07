from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Fname(request):
    return HttpResponse('Enter your name')
