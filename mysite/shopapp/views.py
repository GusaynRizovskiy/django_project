from django.contrib.auth.models import Group
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect,reverse, get_object_or_404
from timeit import default_timer

from django.views import View
from django.views.generic import TemplateView,ListView,DetailView

from shopapp.models import Product, Order
from .forms import GroupForm,ProductForm

class ShopIndexView(View):
    def get(self,request:HttpRequest)->HttpResponse:
        devices = [
            ("Laptop",2900),
            ("Smartphone",4900),
            ("Television",6999)
        ]
        context = {
            "devices": devices
        }
        return render(request,'shopapp/shop-index.html',context = context)

class GroupsView(View):
    def get(self,request:HttpRequest)->HttpResponse:
        context = {
            "form": GroupForm,
            "groups": Group.objects.prefetch_related('permissions').all,
        }
        return render(request,'shopapp/groups-list.html',context = context)
    def post(self,request:HttpRequest)->HttpResponse:
        form = GroupForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(request.path)
class ProductListView(ListView):
    template_name = "shopapp/products-list.html"
    model = Product
    context_object_name = "products"
class ProductDetailsView(View):
    def get(self,request:HttpRequest,pk:int)->HttpResponse:
        product = get_object_or_404(Product,pk=pk)
        context = {
            "product":product
        }
        return render(request,"shopapp/products-details.html",context=context)
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