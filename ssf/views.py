from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html', context={})


def senator_list(request):
    return render(request, 'senators.html', context={})
