from django.http import HttpRequest


def get_user_agent(get_response):
    def middleware(request:HttpRequest):
        print("Before Middleware")
        request.user_agent = request.META.get("HTTP_USER_AGENT")
        response = get_response(request)
        print("After Middleware")
        return response
    return middleware
class schet:
    def __init__(self,get_response):
        self.get_response = get_response
        self.count_request = 0
        self.count_response = 0
        self.count_exception = 0
    def __call__(self, request: HttpRequest):
        self.count_request+=1
        print("request_count = ", self.count_request)
        response = self.get_response(request)
        self.count_response+=1
        print("response_count = ",self.count_response)
        return response
