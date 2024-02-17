from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from timeit import default_timer
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
