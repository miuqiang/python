from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    return HttpResponse('<h1>h1</h1>')

def userInfo(request):
    if request.method == 'POST':
        u=request.POST.get('username',None)
        e=request.POST.get('email',None)
        t=request.POST.get('tel',None)

        models.userInfo.objects.create(username=u,email=e,tel=t)
        
    USER_LIST = models.userInfo.objects.all()
            
    return render(request,'userInfo.html',{'USER_LIST':USER_LIST})
