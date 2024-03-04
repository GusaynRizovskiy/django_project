from django.urls import path
from .views import shop_index,groups,products,orders,create_product
app_name = 'shopapp'
urlpatterns = [
    path('', shop_index,name = 'shop_index'),
    path('groups/',groups,name = 'groups_list'),
    path('products/',products,name = 'products_list'),
    path('orders/', orders, name = 'orders_list'),
    path('products/create/',create_product,name = "product_create")
]
