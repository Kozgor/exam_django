from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from .models import Goods

def index(request):
    goods_list = {
        "items":Goods.objects.all()
    }
    return render(request, 'pages/index.html', goods_list)

def products(request):
    return render(request, 'pages/products.html')

def special_offer(request):
    return render(request, 'pages/special_offer.html')

def product_details(request):
    return render(request, 'pages/product_details.html')

def singleProductDetails(request, product_id):
    product = get_object_or_404(Goods, pk=product_id)
    context ={"product":product} 
    return render(request, 'pages/product_details.html', context=context)

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


