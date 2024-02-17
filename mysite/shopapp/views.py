from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from timeit import default_timer
def shop_index(request: HttpRequest):
    context = {
        "timmer": default_timer
    }
    return render(request,'shopapp/shop-index.html',context = context)
# Create your views here.
