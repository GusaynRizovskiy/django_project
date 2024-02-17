from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
def shop_index(request: HttpRequest):
    return HttpResponse("<b>Hellow World!</b>")
# Create your views here.
