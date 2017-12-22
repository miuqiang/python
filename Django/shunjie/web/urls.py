from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),             #首页
    path('partner/', views.partner, name='partner'), #合作伙伴
    path('about/', views.about, name='about'),       #关于我们
    path('service/', views.service, name='service'), #服务理念
]