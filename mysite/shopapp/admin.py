from io import TextIOWrapper
from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from csv import DictReader
from .admin_mixins import Export_AS_SCV_Mixin
from shopapp.models import Product, Order, ProductImage
from .forms import CSVImportForm
@admin.action(description='Archived products')
def mark_archived(modeladmin: admin.ModelAdmin,request: HttpRequest,queryset:QuerySet):
    queryset.update(archived=True)
@admin.action(description='Unarchived products')
def mark_unarchived(modeladmin: admin.ModelAdmin,request: HttpRequest,queryset:QuerySet):
    queryset.update(archived=False)

class ProductInline(admin.TabularInline):
    model = ProductImage
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin,Export_AS_SCV_Mixin):
    change_list_template = "shopapp/products_changelist.html"
    actions = [
        mark_archived,
        mark_unarchived,
        "export_as_csv"
    ]
    inlines = [
        ProductInline,
    ]
    list_display = 'name','description','price','discount','archived',
    list_display_links = 'name',
    ordering =  'id',
    search_fields = ['name','description']
    fieldsets = [
        (None,{
            'fields': ('name','description')
        }),
        ("Price instructions",{
            'fields': ('price','discount'),
            'classes': ('collapse','wide')
        }),
        ("Extra options", {
            'fields': ('archived',),
            'description': ("You can archived this product or don't do this"),
        }),
        ("Images", {
            'fields': ('preview', ),
        }),
    ]
    def short_description(self,obj:Product):
        if len(obj.description < 48):
            return obj.description
        return obj.description[:48]
    def import_csv(self,request:HttpRequest)-> HttpResponse:
        if request.method == "GET":
            form = CSVImportForm()
            context = {
                "form": form,
            }
            return render(request,'admin/csv_form.html',context)
        form = CSVImportForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {
                "form": form,
            }
            return render(request, 'admin/csv_form.html', context,status=400)
        csv_file = TextIOWrapper(
            form.files["csv_file"].file,
            encoding=request.encoding,
        )
        reader = DictReader(csv_file)
        products = [
            Product(**row)
            for row in reader
        ]
        Product.objects.bulk_create(products)
        self.message_user(request,"Data from csv was imported")
        return redirect("..")
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(
                "import-product-csv",
                self.import_csv,
                name = 'import_product_csv',
            ),
        ]
        return new_urls + urls
# Register your models here.
class OrderInline(admin.TabularInline):
    model = Order.products.through
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline
    ]
    list_display = 'delivery_address','promocode','created_at','user_verbose'
    def user_verbose(self,obj:Order):
        return obj.user.first_name or obj.user.username
    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

