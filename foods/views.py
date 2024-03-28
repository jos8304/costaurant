from django.shortcuts import render
from datetime import datetime
from django.http import Http404
from foods.models import Menu

def index(request):
    context = dict()    
    today = datetime.today().date()
    menus = Menu.objects.all()
    context = {
        "date":today
     }
    context["menus"] = menus
    return render(request,'foods/index.html', context=context)

def food_detail(request,food):
    context = dict()
    if food == "chicken":
        context['name'] = "코딩에 빠진 닭"
        context['desc'] = "주머니가 가벼운 가격"
        context['price'] = 20
        context['img_path'] = "foods/images/chicken.jpg"
    else:
        raise Http404("no menu")
    return render(request, 'foods/detail.html', context = context)
