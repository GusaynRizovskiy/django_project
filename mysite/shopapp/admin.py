from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .admin_mixins import ExportAsCSVMixin
from shopapp.models import Product,Order

class ProductInline(admin.TabularInline):
    model = Product.orders.through
@admin.action(description="Archive products")
def mark_archived(modeladmin: admin.ModelAdmin,request: HttpRequest, queryset: QuerySet):
    queryset.update(archived = True)
@admin.action(description="Unarchive products")
def mark_unarchived(modeladmin: admin.ModelAdmin,request: HttpRequest, queryset: QuerySet):
    queryset.update(archived = False)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin,ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    inlines = [
        ProductInline
    ]
    list_display = "pk", "name", "description_short", "price", "discount",'archived'
    list_display_links = "pk","name"
    ordering = 'pk', 'name'
    search_fields = 'name','description'
    fieldsets = [
        (None,{
            'fields': ('name','description')
        }),
        ('Price options',{
            'fields': ('price',"discount"),
            'classes': ('collapse',"wide"),
        }),
        ("Extra options", {
            'fields': ('archived',),
            'description': ("You can archived this product or don't do this"),
        })
    ]
    def description_short(self,obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'


class OrderInline(admin.TabularInline):
    model = Order.products.through
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline
    ]
    list_display = "delivery_address","promocode","created_at","user_verbose"
    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")
    def user_verbose(self,obj:Order) -> str:
        return obj.user.first_name or Order.user.username
