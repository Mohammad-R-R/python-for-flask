
# from django.shortcuts import render, HttpResponse

# def one_method(request):
#     pass
#     return HttpResponse('hello ')
    
# def another_method(request, my_val):
#     pass
    
# def yet_another(request, name):

#     pass
    
# def one_more(request, id, color):
#     pass
#___________________________________________________________________
#___________________________________________________________________


# from django.shortcuts import HttpResponse, redirect 
# from django.http import JsonResponse
# def root_method(request):
#     return HttpResponse("String response from root_method")

# def another_method(request):
#     return redirect("/redirected_route")
# def redirected_method(request):
#     return JsonResponse({"response": "JSON response from redirected_method", "status": True})

 #___________________________________________________________________
#___________________________________________________________________

from django.shortcuts import render
    
def index(request):
    context = {
    	"name": "moath",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "stat.html", context)


   


