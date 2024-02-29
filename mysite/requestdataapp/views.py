from django.http import HttpRequest
from django.shortcuts import render

def query_params(request: HttpRequest):
    return render(request,'requestdataapp/request-query-params.html')
def request_bio(request: HttpRequest):
    return render(request,'requestdataapp/request-bio-data.html')
# Create your views here.
def new_request_function(request: HttpRequest):
    a = request.GET.get("a","")
    b = request.GET.get("b","")
    result = a+b
    context = {
        "a": a,
        "b": b,
        "result": result,
    }
    return render(request,'requestdataapp/request_some_data.html',context)
