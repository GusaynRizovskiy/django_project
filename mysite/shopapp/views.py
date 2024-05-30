from django.contrib.auth.models import Group
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect,reverse
from timeit import default_timer
from csv import DictWriter
import logging

from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from rest_framework.request import Request
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from shopapp.models import Product, Order
from .forms import GroupForm

from django.utils.decorators import method_decorator
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from shopapp.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from shopapp.common import save_csv_products
log = logging.getLogger(__name__)
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter
    ]
    search_fields =['name','description']
    filterset_fields = [
        'name',
        'description',
        'price',
        'discount',
        'archived'
    ]
    ordering_fields = [
        'name',
        'price',
        'discount',
    ]
    @method_decorator(cache_page(60*2))
    def list(self, request, *args, **kwargs):
        print("hellow product list")
        return super().list(*args,**kwargs)
    @action(methods=['get'],detail=False)
    def download_csv(self,request: Request):
        response = HttpResponse(content_type='text/csv')
        filename = 'product-export.csv'
        response["Content-Disposition"] = f"attachment; filename = {filename}"
        queryset = self.filter_queryset(self.get_queryset())
        fields = [
            'name',
            'description',
            'price',
            'discount',
            'archived'
        ]
        queryset = queryset.only(*fields)
        writer = DictWriter(response, fieldnames=fields)
        writer.writeheader()
        for product in queryset:
            writer.writerow({
                field: getattr(product,field)
                for field in fields
            })
        return response
    @action(
        detail=False,
        methods=["post"],
        parser_classes = [MultiPartParser]
    )
    def upload_csv(self,request: Request):
        products = save_csv_products(
            request.FILES["file"].file,
            encoding=request.encoding,
        )
        serializer = self.get_serializer(products,many = True)
        return Response(serializer.data)

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
        log.debug("Products for shop index: %s", devices)
        log.info("Rendering shop index")
        print("shop index context", context)
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
    queryset = Product.objects.prefetch_related("images")
    context_object_name = "product"

class ProductsCreateView(CreateView):
    model = Product
    fields = "name","description","price","discount","preview"
    success_url = reverse_lazy("shopapp:products_list")

class ProductsUpdateView(UpdateView):
    model = Product
    fields = "name","description","price","discount","preview"
    template_name_suffix = "_update_form"
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shoapp:products_list")

def orders(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related('user').prefetch_related("products").all()
    }
    return render(request,'shopapp/orders-list.html',context = context)