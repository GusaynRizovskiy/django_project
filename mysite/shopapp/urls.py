from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.views.decorators.cache import cache_page
from .views import (
    ShopIndexView,
    ProductDeleteView,
    GroupsView,
    ProductsView,
    orders,
    ProductsCreateView,
    ProductsDetailsView,
    ProductsUpdateView,
    ProductViewSet,
)
routers = DefaultRouter()
routers.register("products",ProductViewSet)
app_name = 'shopapp'
urlpatterns = [
    path('', cache_page(60*3)(ShopIndexView.as_view()),name = 'shop_index'),
    path('api/',include(routers.urls)),
    path('groups/',GroupsView.as_view(),name = 'groups_list'),
    path('products/',ProductsView.as_view(),name = 'products_list'),
    path('products/<int:pk>/',ProductsDetailsView.as_view(),name = 'products_details'),
    path('orders/', orders, name = 'orders_list'),
    path('products/create/',ProductsCreateView.as_view(),name = "product_create"),
    path('products/<int:pk>/update/', ProductsUpdateView.as_view(), name="product_create"),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name="product_confirm_delete"),
]
