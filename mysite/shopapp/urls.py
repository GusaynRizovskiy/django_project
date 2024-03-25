from django.urls import path
from .views import ShopIndexView,ProductDeleteView,GroupsView,ProductsView,orders,ProductsCreateView,ProductsDetailsView,ProductsUpdateView

urlpatterns = [
    path('', ShopIndexView.as_view(),name = 'shop_index'),
    path('groups/',GroupsView.as_view(),name = 'groups_list'),
    path('products/',ProductsView.as_view(),name = 'products_list'),
    path('products/<int:pk>/',ProductsDetailsView.as_view(),name = 'products_details'),
    path('orders/', orders, name = 'orders_list'),
    path('products/create/',ProductsCreateView.as_view(),name = "product_create"),
    path('products/<int:pk>/update/', ProductsUpdateView.as_view(), name="product_create"),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name="product_confirm_delete"),
]
app_name = 'shopapp'
