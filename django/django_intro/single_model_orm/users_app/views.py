from .models import  Users
def index(request):
    context = {
    	"all_the_movies": Users.objects.all()
    }
    return render(request, "show.html", context)