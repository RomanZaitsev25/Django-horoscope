from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def leo(requests):
    return HttpResponse('Это знак зодиака лев')


def scorpio(requests):
    return HttpResponse('Это знак зодиака скорпион')

