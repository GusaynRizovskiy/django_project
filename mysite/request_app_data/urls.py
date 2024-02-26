
from django.contrib import admin
from django.urls import path,include
from .views import process_get_view
app_name = 'request_app_data'
urlpatterns = [
    path('get/',process_get_view, name = 'get-view')
]
