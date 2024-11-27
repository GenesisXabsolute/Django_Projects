from django.shortcuts import render

def index1(request):
    return render(request, 'third_task/main_page.html')

def index2(request):
    return render(request, 'third_task/games_page.html')

def index3(request):
    return render(request, 'third_task/basket_page.html')