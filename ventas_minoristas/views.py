from django.shortcuts import render

def form(request):
    return render(request,'form.html',{})

def producto(request):
    return render(request,'producto.html',{})