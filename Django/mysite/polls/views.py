from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>h1</h1>')

USER_LIST = []
def userInfo(request):
    if request.method=='POST':
        username=request.POST.get('username',None)
        email=request.POST.get('email',None)
        tel=request.POST.get('tel',None)

        if username and email and tel:
            USER_LIST.append({'username':username,'email':email,'tel':tel})
            
    return render(request,'userInfo.html',{'USER_LIST':USER_LIST})

