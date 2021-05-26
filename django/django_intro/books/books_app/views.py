from django.db import reset_queries
from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,"book.html")

def booky(request):
    return render(request,"book.html")