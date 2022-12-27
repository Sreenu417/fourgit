from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sreenu(request):
    return HttpResponse('<h1>my favourite criketer is MS Dhoni</h1>')


def raj(request):
    return HttpResponse('<h1>Jspiders</h1>')