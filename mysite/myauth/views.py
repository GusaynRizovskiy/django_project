from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View,CreateView,TemplateView

from myauth.models import Profile


class AboutMe(TemplateView):
    template_name = 'myauth/about-me.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user = self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password)
        login(request = self.request,user = user)
        return response


#
# def LoginView(request:HttpRequest):
#     if request.method=="GET":
#         if request.user.is_authenticated:
#             return redirect("/admin/")
#         return render(request,"myauth/login.html")
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request,username=username,password=password)
#     if user:
#         login(request,user)
#         return redirect("/admin/")
#     return render(request,"myauth/login.html", {"error":"Invalid username or password"})
# # Create your views here.
# class MyLogoutView(LogoutView):
#     next_page = reverse_lazy("myauth:login")
def logout_view(request):
    logout(request)
    return redirect(reverse('myauth:login'))
def get_coockie(request:HttpRequest)->HttpResponse:
    value = request.COOKIES.get("foobar")
    return HttpResponse(f"Coockie get: {value}")
def set_coockie(request:HttpRequest)->HttpResponse:
    response = HttpResponse("Coockie set")
    response.set_cookie("foobar","bananas",max_age=3600)
    return response

class FooBarView(View):
    def get(self,request:HttpRequest):
        return JsonResponse({"fruit":"apple","orange":"bananas"})
