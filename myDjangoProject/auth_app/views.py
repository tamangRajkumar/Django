from pydoc import doc
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def register(request):
        # return HttpResponse("Register User")
        # return render("This")
        return render(request, 'auth_app/html/register/register.html')

def login(request):
        return render(request, 'auth_app/html/login/login.html' )
        