from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

# Create your views here.
def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a',"")
    b = request.GET.get('b',"")
    result = a+b
    context = {
        "result": result,
        'a': a,
        'b': b,
    }
    return render(request,'request_app_data/request-query-params.html', context)