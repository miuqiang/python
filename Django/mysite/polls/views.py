from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>h1</h1>')

def userInfo(request):
    return render(request,'userInfo.html')

