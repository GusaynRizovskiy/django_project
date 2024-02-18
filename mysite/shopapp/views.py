from django.contrib.auth.models import Group
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from timeit import default_timer
from shopapp.models import Product, Order


def shop_index(request: HttpRequest):
    devices = [
        ("Laptop",2900),
        ("Smartphone",4900),
        ("Television",6999)
    ]
    context = {
        "devices": devices
    }
    return render(request,'shopapp/shop-index.html',context = context)
# Create your views here.
def groups(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all,
    }
    return render(request,'shopapp/groups-list.html',context = context)
def products(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request,'shopapp/products-list.html',context=context)
def orders(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related('user').prefetch_related("products").all()
    }
    return render(request,'shopapp/orders-list.html',context = context)