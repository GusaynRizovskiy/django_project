from django.urls import path
from .views import shop_index,groups

urlpatterns = [
    path('', shop_index,name = 'shop_index'),
    path('groups/',groups,name = 'groups-list'),
]
