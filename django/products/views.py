from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Offer

# Create your views here.
def index(request):
    products=Product.objects.all();
    return render(request,'index.html',{'products':products})
    #return HttpResponse('<h1> Welcome To Django </h1>')

def offerindex(request):
    offers=Offer.objects.all();
    return render(request,'offerindex.html',{'offers': offers})
    #return HttpResponse('<h1> Welcome To Django </h1>')


def about(request):
     return HttpResponse('<h1> About Page </h1>')

def contacts(request):
    return HttpResponse('<h1>Shibu Varghese</h1><h2>springfield</h2><h3>penang</h3>')
