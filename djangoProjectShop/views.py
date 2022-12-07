from django.shortcuts import render
from db.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'test.html',{"products":products})

def new(request):
    return render(request, 'new.html')