from django.contrib import admin

from shopapp.models import Product, Order


class ProductInline(admin.TabularInline):
    model = Product.orders.through
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = 'name','description','price','discount'
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
        ("Extra information", {
            'fields': ('archived'),
            'description': ('Extra information for you.',),
        })
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

