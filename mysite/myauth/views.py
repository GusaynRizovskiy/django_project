from django.contrib.auth import authenticate,login
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View


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

def get_coockie(request:HttpRequest)->HttpResponse:
    value = request.COOKIES.get("foobar","default_value")
    return HttpResponse(f"Coockie get: {value}")
def set_coockie(request:HttpRequest) -> HttpResponse:
    response = HttpResponse("Coockie set")
    response.set_cookie("foobar","dady",max_age=1000)
    return response

class FooBarView(View):
    def get(self)->JsonResponse:
        return JsonResponse({"putin":"good","baiden":"evil"})
