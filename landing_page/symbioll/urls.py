from django.urls import path
from symbioll.views import index

urlpatterns=[
    path('index/', index, name='index'),
]