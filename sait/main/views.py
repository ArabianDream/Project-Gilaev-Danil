from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>Сайт Гилаева Данила 9В</h4>')


def about(request):
    return HttpResponse('<h4>Про сайт</h4>')