from django.shortcuts import render

def index1(request):
    return render(request, 'second_task/func.html')

def index2(request):
    return render(request, 'second_task/class.html')

def index3(request):
    return render(request, 'second_task/class_func.html')
