from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def products(request):
    return render(request, 'products.html')
def login(request):
    return render(request, 'login.html')
def singleproduct(request):
    return render(request, 'single-product.html')

def navbar(request):
    return render(request, 'nav.html')