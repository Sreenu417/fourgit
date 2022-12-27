from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def pavan(request):
    return HttpResponse('<h1><marquee>My favourite actor is NTR</h1></marquee>')