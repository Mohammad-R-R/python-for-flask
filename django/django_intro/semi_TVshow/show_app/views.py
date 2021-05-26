from django.shortcuts import redirect, render, HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    print("hey")
    return redirect("/show")

def add(request):
    #show1=show.objects.create(title=request.POST['title'],network=request.POST['Network'],date=request.POST['date'],Description=request.POST['Descrption'])
    return render(request,'add_show.html')

def theadd(request):
    Show.objects.create(title=request.POST['title'],network=request.POST['Network'],date=request.POST['date'], Description=request.POST['Description'])
    lastshow=Show.objects.last()
    id=lastshow.id
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
        
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
            return redirect("/")
    else:
        messages.success(request, "Blog successfully updated")




    return redirect(f'/shows/{id}')

def theshow(request,num):
    print("hello")
    context={'to_show': Show.objects.get(id=num)
    }
    return render(request,'one_show.html',context)

def to_print(request):
    context={'all_shows': Show.objects.all()}
    return render(request,'all_shows.html',context)

def the_edit(request,id):
    context={
        'show':Show.objects.get(id=id)
    }
    return render(request,'edit.html',context)

def edit(request,id):

    x= Show.objects.get(id=id)
    x.title = request.POST['title']
    x.network = request.POST['Network']
    x.date = request.POST['date']
    x.Description = request.POST['Description']
    x.save()

    return redirect(f'/shows/{id}')


def delete(request,id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')
    

