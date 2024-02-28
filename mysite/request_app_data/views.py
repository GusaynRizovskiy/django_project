from django.core.files.storage import FileSystemStorage
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
def user_form(request: HttpRequest)->HttpResponse:
    return render(request,'request_app_data/request-bio-form.html')
def handle_file_upload(request: HttpRequest)->HttpResponse:
    if request.method == "FILES" and request.POST.get("myfile"):
        myfile = request.FILES["myfile"]
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name,myfile)
        print("saved file",file_name)

    return render(request,'request_app_data/file-upload.html')