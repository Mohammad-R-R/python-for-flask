from django.shortcuts import redirect, render, HttpResponse

def index(request):
    request.session['counter']=0
   
    return redirect('/count')

def count1(request):
    count = request.session['counter']
    count = count+1
    request.session['counter']=count
    context={
        'counter':request.session['counter']
    }
    return render(request,"show.html",context)

def destroy(request):
   
    return redirect('/')

