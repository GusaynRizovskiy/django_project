from django.contrib.auth.models import Group
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect,reverse
from timeit import default_timer

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView

from shopapp.models import Product, Order
from .forms import GroupForm

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
# Create your views here.
class GroupsView(View):
    def get(self,request:HttpRequest)->HttpResponse:
        context = {
            "form": GroupForm,
            "groups": Group.objects.prefetch_related('permissions').all,
        }
        return render(request,'shopapp/groups-list.html',context = context)
    def post(self,request:HttpRequest) -> HttpResponse:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)
class ProductsView(ListView):
    template_name = 'shopapp/products-list.html'
    model = Product
    context_object_name = "products"
class ProductsDetailsView(DetailView):
    template_name = 'shopapp/products-details.html'
    model = Product
    context_object_name = "product"

class ProductsCreateView(CreateView):
    model = Product
    fields = "name","description","price","discount"
    success_url = reverse_lazy("shopapp:products_list")

class ProductsUpdateView(UpdateView):
    model = Product
    fields = "name","description","price","discount"
    template_name_suffix = "_update_form"
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shoapp:products_list")

def orders(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related('user').prefetch_related("products").all()
    }
    return render(request,'shopapp/orders-list.html',context = context)