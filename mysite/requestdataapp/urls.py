from django.urls import path,include
from .views import query_params,request_bio,new_request_function
urlpatterns = [
    path('params/',query_params,name = 'query_params'),
    path('bio/',request_bio,name = 'request_bio'),
    path('data/',new_request_function,name = 'new_data')
]
