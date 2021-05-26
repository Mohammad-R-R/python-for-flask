from django.urls import path     
from . import views
urlpatterns = [
    path('', views.add),
    path('shows/new',views.theadd),
    path('shows/<int:num>',views.theshow),
    path('shows',views.to_print),
    path('shows/<int:id>/edit',views.the_edit),
    path('shows/<int:id>/update',views.edit),
    path('delete/<int:id>',views.delete)
]