from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from .forms import UserBioForm,UploadFileForm
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
    context = {
        'form': UserBioForm()
    }
    return render(request,'request_app_data/request-bio-form.html',context = context)
def handle_file_upload_with_size(request: HttpRequest)->HttpResponse:
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            myfile = form.cleaned_data["file"]
            fs = FileSystemStorage()
            file_name = fs.save(myfile.name,myfile)
            file_size = fs.size(file_name)
            if file_size>1048576:
                fs.delete(file_name)
                print("file is deleted",file_name)
                return render(request,"request_app_data/error_size_file.html")
            else:
                print("file is saved with name ",file_name)
    else:
        form = UploadFileForm()
    context = {
        "form": form
    }
    return render(request,'request_app_data/file-upload.html',context=context)