from django.contrib.auth.views import LoginView
from django.urls import path
from .views import get_coockie,set_coockie,FooBarView, AboutMe, logout_view,RegisterView
app_name = 'myauth'
urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='myauth/login.html',
        redirect_authenticated_user=True,
    ),name="login"),
    path('logout/',logout_view, name = 'logout'),

    path('foobar/',FooBarView.as_view(),name='foo-bar'),
    path('about_me/',AboutMe.as_view(),name='about-me'),
    path('register/',RegisterView.as_view(),name = 'register'),

    path('get_coockie/',get_coockie,name='get_coockie'),
    path('set_coockie/',set_coockie,name='set_coockie'),
]
