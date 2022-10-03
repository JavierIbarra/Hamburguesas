from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    context={}
    return(render(request,'home.html',context=context))
    
