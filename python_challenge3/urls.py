from django.urls import include, path
from rest_framework import routers

from . import views
import os


urlpatterns =[
    path('', views.phone_numbers_list),
    path('search/<str:areacode>', views.filter_number)
]





