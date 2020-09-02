from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Goods

def index(request):
    return render(request, 'pages/index.html')

def products(request):
    return render(request, 'pages/products.html')

def special_offer(request):
    return render(request, 'pages/special_offer.html')

def product_details(request):
    return render(request, 'pages/product_details.html')

def compair(request):
    return render(request, 'pages/compair.html')

def summary(request):
    return render(request, 'pages/product_summary.html')

def login(request):
    return render(request, 'pages/login.html')

def forgetpass(request):
    return render(request, 'pages/forgetpass.html')

def register(request):
    return render(request, 'pages/register.html')

def contact(request):
    return render(request, 'pages/contact.html')

def normalinfo(request):
    return render(request, 'pages/normal.html')

def faq(request):
    return render(request, 'pages/faq.html')

class GoodsView(View):
    def get(self, request):
        goods_list = Goods.objects.all()
        return render(request, "pages/index.html", {"goods_list":goods_list})
