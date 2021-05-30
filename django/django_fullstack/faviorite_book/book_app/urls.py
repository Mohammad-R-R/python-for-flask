from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('login',views.the_log),
    path('reg',views.reg),
    path('logout',views.logout),
    path('add_book',views.add_book),
    path('welcome',views.welcome),
    path('books/<int:id>',views.view_book),
    path('update/<int:id>',views.update),
    path('addto_fav/<int:id1>/<int:id2>',views.fav_book)

]