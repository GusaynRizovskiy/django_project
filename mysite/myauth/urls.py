from django.contrib.auth.views import LoginView
from django.urls import path
from .views import get_coockie, set_coockie,FooBarView


app_name = 'myauth'
urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='myauth/login.html',
        redirect_authenticated_user=True,
    ),name="login"),
    path('set_coockie/', set_coockie,name = "set_cookie"),
    path('get_coockie/', get_coockie,name = "get_cookie"),
    path('foobar/', FooBarView.as_view(),name = "foo-bar"),
]