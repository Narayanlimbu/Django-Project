from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>This is Home page</h1>")


def login(request):
    return render(request, 'login.html')

def abt(request):
    return render(request, 'about.html')