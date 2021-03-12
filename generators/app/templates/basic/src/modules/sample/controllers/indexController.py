from django.shortcuts import render
from django.http import HttpResponse

#https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
def index(request):
    html = "<html><body>sample module Index page</body></html>"
    return HttpResponse(html)
