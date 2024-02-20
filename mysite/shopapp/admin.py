from django.contrib import admin

from shopapp.models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'name','description','price','discount'
    list_display_links = 'name',
    ordering =  'id',
    search_fields = ['name','description']
    def short_description(self,obj:Product):
        if len(obj.description < 48):
            return obj.description
        return obj.description[:48]

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'delivery_address','promocode','created_at','user_verbose'
    def user_verbose(self,obj:Order):
        return obj.user.first_name or obj.user.username

