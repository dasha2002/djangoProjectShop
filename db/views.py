from django.shortcuts import render
from db.models import Product

def db_home(request):
    return render(request, 'test.html')

def addInCart(request, idProduct):
    t = Product.objects.get(id=idProduct)
    t.choose = True
    t.save()


def deleteFromCart(request, idProduct):
    t = Product.objects.get(id=idProduct)
    t.choose = False
    t.save()

