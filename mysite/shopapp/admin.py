from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .admin_mixins import Export_AS_SCV_Mixin
from shopapp.models import Product, Order, ProductImage
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

