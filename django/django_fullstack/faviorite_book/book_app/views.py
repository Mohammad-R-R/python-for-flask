from django.shortcuts import redirect, render,HttpResponse
from . import models
from book_app.models import *
from django.contrib import messages
import bcrypt

def index (request):
    if "id" in request.session:
        return redirect('/welcome')
    return render(request,'index.html')

def reg(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
    else:
        
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        print(pw_hash)
        
        Users.objects.create(first_name= request.POST['first_name'],last_name = request.POST['last_name'],email=request.POST['email'],password=pw_hash)
        

        users=Users.objects.filter(email=request.POST['email'])
        logged_user=users[0]
        request.session['user']={
            'id':logged_user.id,
            'firstname':logged_user.first_name,
            'last_name':logged_user.last_name,
            'email':logged_user.email
                        }
        return redirect('/welcome')

def the_log(request):

    errors2 = Users.objects.basic_validator2(request.POST)
            
    if len(errors2) > 0:
            
        for key, value in errors2.items():
            messages.error(request, value)
            print("the error1")
        return redirect('/')
    else:
        # password=request.POST['password1']
        email=request.POST['email2']
        user =Users.objects.filter(email=email)
        print("the error12")
        
        if user:
            k=user[0]
            request.session['id']=k.id
            request.session['name']=k.first_name
            print("the error123")
            if bcrypt.checkpw(request.POST['password1'].encode(), k.password.encode()):
                print("password match")
                
                return redirect("/welcome")
                
            # return HttpResponse('it looged ')
            else:
                print("failed password")
    
                return HttpResponse('password error')
        else:
            return HttpResponse('nothing')
        
def logout(request):
    request.session.clear()
    return redirect("/")

def welcome(request):
    if "id" not in request.session:
        
        return redirect('/')
    context={
        'x':Book.objects.all(),
        'z':Users.objects.get(id=request.session['id'])
    }
    
    return render(request,'welcome.html',context)

def add_book(request):
    # print(request.method)
    # print(request.POST)
    errors = Book.objects.basic_validator(request.POST)
    # print("_" * 30)
            
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            print("the error1")
        return redirect('/welcome')
    else:
        user=Users.objects.get(id=request.session['id'])
        Book.objects.create(title=request.POST['title'],desc=request.POST['desc'],uploaded_by=user)
    return redirect('/welcome')


def view_book(request,id):
    

    context={
       'book_edit':Book.objects.get(id=id),
       'username':Users.objects.get(id=request.session['id'])

    }
    return render(request,"temp.html",context)

def update(request,id):
    edit=Book.objects.get(id=id)
    edit.desc=request.POST['test']
    edit.save()
    return redirect('/books/'+ str(id))
 
def fav_book(request,id1,id2):
    user=Users.objects.get(id=id1)
    book=Book.objects.get(id=id2)
    book.users_who_like.add(user)
    return redirect('/welcome')




    
