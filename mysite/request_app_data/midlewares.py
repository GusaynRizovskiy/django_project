import time

from django.http import HttpRequest
from django.shortcuts import render


def middleware(get_response):
    print("Begin middleware")
    def middleware(request:HttpRequest):
        print("Before middleware")
        request.user_agent = request.META.get("HTTP_USER_AGENT")
        response = get_response(request)
        print("Afret middleware")
        return response
    return middleware

# class CountRequestMiddleware:
#     def __init__(self,get_response)->None:
#         self.get_response = get_response
#         self.request_count = 0
#         self.response_count = 0
#         self.exception_count = 0
#         self.request_time ={}
#     def __call__(self, request: HttpRequest):
#         time_delay = 10
#         if not self.request_time:
#             print("Это первый request после перезапуска сервера, словарь еще пуст")
#         else:
#             if (round(time.time())*1) - self.request_time["time"]<time_delay \
#                      and self.request_time["ip_address"]==request.META.get("REMOTE_ADDR"):
#                 print("Прошло меньше 10 секунд для повторного запроса с вашего ip адреса")
#                 return render(request,'request_app_data/error-time-request.html')
#         self.request_time = {"time":round(time.time())*1,"ip_address":request.META.get("REMOTE_ADDR")}
#         self.request_count+=1
#         print("request count: ",self.request_count)
#         response = self.get_response(request)
#         self.response_count+=1
#         print("response count:",self.response_count)
#         return response

