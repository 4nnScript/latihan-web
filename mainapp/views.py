from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def landing_page(request):
    return HttpResponse("Hello, World! Nama Saya Ariq")


def profile(request):
    return HttpResponse("profile ku")


def count(request, angka):
    angka = angka+1
    return HttpResponse(str(angka))


def sapa(request, nama):
    return HttpResponse("Halo "+nama)


def example(request):
    return render(request, 'example.html')


def newpage(request):
    return HttpResponse("new")


def a(request):
    return HttpResponse()


def shop(request):
    return render(request, 'shop.html')


def shop_laptop(request):
    return render(request, 'shop_laptop.html')


def shop_console(request):
    return render(request, 'shop_console.html')


def shop_smartphone(request):
    return render(request, 'shop_smartphone.html')


def first_page(request):
    return render(request, 'firstpage.html')


def second_page(request):
    return render(request, 'secondpage.html')

def buy (request):
    return render (request, "buy.html")

def home (request):
    return render (request, "home.html")

def wedding(request):
    return render (request, "wedding.html")

def laptop_list(request):
# try:
    catagory_laptop = Catagory.objects.get(pk=1)
    product_laptop = Product.objects.filter(catagory=catagory_laptop)
    return render(request, 'shop_laptop_list.html', {'product_list': product_laptop})
# except:
#     return HttpResponse("Terjadi Error")



