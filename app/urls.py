from django.urls import path
from app.views import *
app_name='sreenu'
urlpatterns=[
    path('sreenu/',sreenu,name='sreenu'),
    path('raj/',raj,name='raj'),
]