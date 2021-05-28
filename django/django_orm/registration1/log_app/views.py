from io import RawIOBase
from django.db import models
from django.shortcuts import redirect, render, HttpResponse
def index(request):
    return render(request,"show.html")

def login(request):
    if request.method == "POST":
        if request.POST["login_type"]=="login":
         models.r
        if request.POST["login_type"]=="login":
         pass
   
    return redirect("/")
    