from django.contrib.auth.models import Group
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect,reverse
from timeit import default_timer
from shopapp.models import Product, Order
from .forms import ProductForm

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
def create_product(request:HttpRequest)->HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # Product.objects.create(**form.cleaned_data)
            url = reverse("shopapp:products_list")
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request,'shopapp/create-product.html',context=context)