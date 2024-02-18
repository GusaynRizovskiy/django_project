from django.contrib.auth.models import Group
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from timeit import default_timer
from shopapp.models import Product
def shop_index(request: HttpRequest):
    devices = [
        ("Laptop",2900),
        ("Smartphone",4900),
        ("Television",6999)
    ]
    context = {
        "timmer": default_timer,
        "devices": devices
    }
    return render(request,'shopapp/shop-index.html',context = context)
# Create your views here.
def groups(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all,
        "timmer": default_timer,
    }
    return render(request,'shopapp/groups-list.html',context = context)
def products(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
        "timmer": default_timer,
    }
    return render(request,'shopapp/products-list.html',context=context)