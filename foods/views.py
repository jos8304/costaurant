from django.shortcuts import render
from datetime import datetime

def index(request):
    today = datetime.today().date()
    context = {
        "date":today
     }
    return render(request,'foods/index.html', context=context)

def food_detail(request,food):
    context = dict()
    if food == "chicken":
        context['name'] = "코딩에 빠진 닭"
        context['desc'] = "주머니가 가벼운 가격"
        context['price'] = 20
        context['img_path'] = "foods/images/chicken.jpg"
    return render(request, 'foods/detail.html', context = context)
