from django.http import HttpResponse

class YehiaMiddleWare(object):
    def __init__(self, get_response):
        print("inside middleware")


