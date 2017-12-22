from django.shortcuts import render

# Create your views here.
#首页
def index(req):
    return render(req,'index.html')
#合作伙伴
def partner(req):    
    return render(req,'partner.html')
# 关于我们
def about(req):
    return render(req,'about.html')
# 关于我们
def service(req):
    return render(req,'service.html')