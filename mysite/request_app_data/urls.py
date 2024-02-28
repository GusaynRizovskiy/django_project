
from django.contrib import admin
from django.urls import path,include
from .views import process_get_view,user_form,handle_file_upload
app_name = 'request_app_data'
urlpatterns = [
    path('get/',process_get_view, name = 'get-view'),
    path('bio/',user_form, name = 'user-form'),
    path('upload/',handle_file_upload,name='file-upload')
]
