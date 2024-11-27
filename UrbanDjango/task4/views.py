from django.shortcuts import render

def index1(request):
    return render(request, 'fourth_task/main_page.html')

def index2(request):
    context =  {'games': ['Atomic Heart', "Cyberpunk 2077"]}
    return render(request, 'fourth_task/games_page.html', context)

def index3(request):
    return render(request, 'fourth_task/basket_page.html')