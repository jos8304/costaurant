from django.shortcuts import render
from datetime import datetime

def index(request):
    today = datetime.today().date()
    context = {
        "date":today
     }
    return render(request,'foods/index.html', context=context)

