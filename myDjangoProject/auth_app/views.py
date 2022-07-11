from pydoc import doc
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def register(request):
        # return HttpResponse("Register User")
        return render(request, 'auth_app/register.html')


        