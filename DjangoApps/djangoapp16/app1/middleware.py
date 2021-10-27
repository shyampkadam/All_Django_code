class MiddleWare1(object):
    def __init__(self,get_response):
        print('*****__init__*****')
        self.get_response=get_response
    def __call__(self, request):
        print('*****Before request processing to view*****')
        response=self.get_response(request)
        print('*****After response processing from view**********')
        return  response

from django.http import HttpResponse
class ExceptionHanlderMiddleWare(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        return self.get_response(request)
    def process_exception(self,request,exception):
        return HttpResponse("<h1>Having Issue at server side</h1>")