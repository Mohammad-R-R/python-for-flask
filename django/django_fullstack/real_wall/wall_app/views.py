from django.shortcuts import redirect, render,HttpResponse
from . import models
from login_app.models import *
from django.contrib import messages
import bcrypt

def index (request):
    return render(request,'index.html')

def reg(request):

        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
   

        errors = Users.objects.basic_validator(request.POST)
            
        if len(errors) > 0:
            
            for key, value in errors.items():
                messages.error(request, value)
           
            return redirect('/')
        else:
            # request.session['user']={
            #     'email':request.POST['email'],
            #     'password':request.POST['password']
            # }
            # blog = Users.objects.get(id = id)
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
            print(pw_hash)
            Users.objects.create(first_name= request.POST['first_name'],last_name = request.POST['last_name'],email=request.POST['email'],password=pw_hash)
            users=Users.objects.filter(email=request.POST['email'])
            logged_user=users[0]
            # secondlog=users[1]
            
            # if logged_user.email==secondlog.email :
            #     print("allready exisit")
            request.session['user']={
                'id':logged_user.id,
                'firstname':logged_user.first_name,
                'last_name':logged_user.last_name,
                'email':logged_user.email
                            }
            return render(request,'welcome.html')

def check(request):
    if 'user' in request.session:
        return render(request,"welcome.html")
    return redirect('/login')



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
        # user = Users.objects.get(email=request.POST['email2'])
        # user2=Users.objects.filter
        # emaill=user[0].email
        # passd = Users.objects.filter(k.password)=)
        # passl=passd[0].password
        if user:
            k=user[0]
            print("the error123")
            if bcrypt.checkpw(request.POST['password1'].encode(), k.password.encode()):
                print("password match")
                return render(request,'welcome.html')
                
            # return HttpResponse('it looged ')
            else:
                print("failed password")
    
                return HttpResponse('password error')
        else:
            return HttpResponse('nothing')
        
def logout(request):
    request.session.flush()
    return redirect("/")