from django.urls import path
from .views import shop_index,groups,products

urlpatterns = [
    path('', shop_index,name = 'shop_index'),
    path('groups/',groups,name = 'groups_list'),
    path('products',products,name = 'products_list')
]
