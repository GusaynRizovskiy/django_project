from django.http import HttpRequest


def middleware(get_response):
    print("Begin middleware")
    def middleware(request:HttpRequest):
        print("Before middleware")
        request.user_agent = request.META.get("HTTP_USER_AGENT")
        response = get_response(request)
        print("Afret middleware")
        return response
    return middleware

class CountRequestMiddleware:
    def __init__(self,get_response)->None:
        self.response = get_response
        self.request_count = 0
        self.response_count = 0
        self.exception_count = 0
    def __call__(self, request: HttpRequest):
        self.request_count+=1
        print("request_count = ",self.request_count)
        response = self.response(request)
        self.response_count+=1
        print("response_count = ", self.response_count)
        return response
