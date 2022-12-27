from django.urls import path
from app1.views import *
app_name='pavan'
urlpatterns=[
    path('pavan/',pavan,name='pavan'),
]