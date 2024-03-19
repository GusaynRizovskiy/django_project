from django.urls import path
from .views import OrderDetailsView,ShopIndexView,GroupsView,ProductListView,OrdersListView,create_product,ShopIndexView,ProductDetailsView

app_name = 'shopapp'
urlpatterns = [
    path('', ShopIndexView.as_view(),name = 'shop_index'),
    path('groups/',GroupsView.as_view(),name = 'groups_list'),
    path('products/',ProductListView.as_view(),name = 'products_list'),
    path('products/<int:pk>/',ProductDetailsView.as_view(),name = 'products_details'),
    path('orders/', OrdersListView.as_view(), name = 'orders_list'),
    path('orders/<int:pk>', OrderDetailsView.as_view(), name = 'orders_details_view'),
    path('products/create/',create_product,name = "product_create"),
]
