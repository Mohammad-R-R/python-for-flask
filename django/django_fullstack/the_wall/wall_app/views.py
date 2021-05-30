from django.shortcuts import redirect, render
from .models import*
from django.contrib import messages
from datetime import date, datetime, timedelta
from django.utils import timezone
def home(req):
    req.session['user'] = ""
    req.session['mymessages'] = ""
    return render(req,"home.html")
def createuser(req):
    errors = User.objects.basic_validator(req.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(req, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        firstname = req.POST['firstname']
        lastname = req.POST['lastname']
        email = req.POST['email']
        passwd = req.POST['passwd']
        confpw = req.POST['confirmpw']
        birthDate = req.POST['birth_date']
        try:
            if User.objects.get(email=email):
                errors["retitle"] = "this email is already exist"
        except:
            pass
        if passwd == confpw :
            User.objects.create(first_name=firstname,last_name=lastname,email=email,passwod=passwd)
            data ={
                "fname":firstname,
                "lastname":lastname,
                "email": email,
                "pass":passwd,
                "birth_date": birthDate
            }
            req.session['user'] = data
            return redirect('/welcome')
        return redirect("/")
def login(req):
    errors = User.objects.login_Validator(req.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(req, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        email = req.POST['loginemail']
        passwd = req.POST['loginpass']
        users = User.objects.filter(email=email)
        
        if len(users) == 0:
            return redirect("/")
        user = users.first()
        if user.passwod != passwd:
            return redirect("/")
        data ={
            'fname' : user.first_name,
            'password':user.passwod,
            'email' : user.email,
            'lastname' : user.last_name,
            'userid':user.id
        }
        req.session['user']= data
        return redirect("/welcome")

def welc(req):
    all_messages = Messages.objects.all()
    #all_comment = Comments.objects.all()
    if req.session['user'] :
        user = req.session['user']
        data={
        'my_massege':all_messages,
        'user':user,
        #'comments':all_comment
        }
        
        return render(req,"welcome.html",data)
    return redirect('/')
def logout(req):
    if req.session['user']:
        req.session.clear()
        return redirect('/')
def creatmessage(req):
    users = User.objects.filter(first_name = req.session['user']['fname'])
    user = users[0]
    message =req.POST['messagearea']
    if len(message) != 0:
        Messages.objects.create(message =  message, user = user )
        #all_messages = Messages.objects.all()
        data = {
            "mymessag" : message,
            
        }
        req.session['mymessages'] = data
        return redirect('/welcome')
def delete_message(req,id):
    users = User.objects.filter(first_name = req.session['user']['fname'])
    user = users[0]
    message_for_delete = Messages.objects.filter(id=id , user = user  )
    message_for_delete.delete()
    return redirect('/welcome')

def showCommenits(req,id):
    all_messages = Messages.objects.filter(id=id)
    all_messages.first()
    users = req.session['user']
    myCommints = Comments.objects.filter(message = all_messages[0] )
    if req.session['user']:
        user = req.session['user']
        data={
        'my_commints':myCommints,
        'user':user,
        'my_massege': all_messages
        }
    return render(req,'profile.html',data)
def createComment(req,id):
    comment = req.POST['mycomment']
    users = User.objects.filter(first_name = req.session['user']['fname'])
    user = users[0]
    messages = Messages.objects.filter(id = id)
    message = messages.first()
    Comments.objects.create(comment = comment ,user = user , message = message )
    return redirect('/welcome')
def deletcomment(req,id):
    users = User.objects.filter(first_name = req.session['user']['fname'])
    user = users[0]
    Commentfordelet = Comments.objects.filter(id=id , user = user) 
    Commentfordelet.delete()
    return redirect('/welcome')
