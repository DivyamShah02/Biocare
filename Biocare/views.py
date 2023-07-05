from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import random,datetime,json
from PIL import Image


def error(request):
    return render(request,'404.html')

def home(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def blogs(request):
    return render(request,'blog.html')

def contact_us(request):
    return render(request,'contact.html')

def products(request):
    return render(request,'products.html')

def product_info(request):
    return render(request,'product_info.html')

def sign_in(request):
    return render(request,'sign_in.html')

def register(request):
    return render(request,'register.html')

def blog_single(request):
    return render(request,'blog_single.html')