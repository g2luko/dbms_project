from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path("sports/",views.sports,name="sports"),
    
    path("dropdown/", views.dropdown,name="dropdown"),

    path("results/", views.results, name="results"),

    path("login/",views.logging,name="login"),

    path("logout/",views.logout, name="logout"),

    path("menu/",views.menu, name="menu"),

    path("table/",views.table, name="table"),

]
    