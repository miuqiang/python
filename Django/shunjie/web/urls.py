from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('/partner', views.partner, name='partner'), #合作伙伴
]