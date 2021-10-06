from todolist.views import delete, home
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('about', views.about, name="about"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('crossoff/<list_id>', views.crossoff, name="crossoff"),
    path('uncross/<list_id>', views.uncross, name="uncross"),
    path('edit/<list_id>', views.edit, name="edit"),
    

]
