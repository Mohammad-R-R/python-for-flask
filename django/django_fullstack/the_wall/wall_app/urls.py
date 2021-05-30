from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('create',views.createuser),
    path('welcome',views.welc),
    path('login',views.login),
    path('logout',views.logout),
    path('message',views.creatmessage),
    path('delet_message/<int:id>',views.delete_message),
    path('showCommenits/MakeComment/<int:id>',views.createComment),
    path('showCommenits/<int:id>',views.showCommenits),
    path('showCommenits/deletcomment/<int:id>', views.deletcomment)
    
]