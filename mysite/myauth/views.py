from django.contrib.auth import authenticate,login
from django.http import HttpRequest, HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.views import View


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

def get_coockie(request:HttpRequest):
    value = request.COOKIES.get("fizz","default_name")
    return HttpResponse(f"Coockie value: {value!r}")
def set_coockie(request:HttpRequest):
    response = HttpResponse("Set Coockie")
    response.set_cookie("fizz","buzz")
    return response

class FooBarView(View):
    def get(self,request:HttpRequest)->JsonResponse:
        return JsonResponse({"foo":"bar","spam":"eggs"})