
class YehiaMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(self.get_response(request))
        return self.get_response(request)

    def process_exception(self, request, exception): 
        print("Inside middleware")
        return None

