from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'bot_back_end/index.html')


def about(request):
    return render(request, 'bot_back_end/about.html')