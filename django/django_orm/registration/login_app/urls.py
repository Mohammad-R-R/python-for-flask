from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('login',views.the_log),
    path('reg',views.reg),
    path('logout',views.logout)

]