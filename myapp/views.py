from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("This is Our Home Page")

def about(request):
    return HttpResponse("This is Our About Page")

def contact(request):
    return HttpResponse("This is Our Contact Page")

def service(request):
    return HttpResponse("This is Our Service Page")