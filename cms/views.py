from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def news(request):
    return render(request, 'news.html')


def acade(request):
    return render(request, 'acade.html')


def member(request):
    return render(request, 'member.html')