from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.form,name='form'),
    path('producto/',views.producto,name="producto"),
]
