from turtle import home
from unicodedata import name
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view,name="home"),
    path('single-page/',views.detail_view,name="single-page"),
]
