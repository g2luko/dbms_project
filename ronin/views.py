from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,logout

from django.contrib import messages
# Create your views here.


# message =[
#     {"name":"gokul","email":"gokul@gmail.com"}
# ]
def logout(request):

    auth.logout(request)
    return redirect("/")



def index(request):

    return render(request,"index.html")

def logging(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        global user
        user = authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("http://127.0.0.1:8000/ronin/dropdown/")
        else:
            messages.info(request, 'Wrong username or password')
            return redirect("http://127.0.0.1:8000/ronin/login/")
    else:
        return render(request,'login.html')


def sports(request):
    if request.method == 'POST':
        username= request.POST['username']
        passowrd= request.POST['password']
        user = authenticate(username=username,passowrd=passowrd)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credientials")
            return redirect('sports')
    else:
        return render(request,'sports_index.html')


def menu(request):
    return render(request,"menu.html")

def table(request):
    return render(request,"table.html")
@login_required
def dropdown(request):
    return render(request,"dropdown.html")

def results(request):
    if request.GET['sports']=='kabadi':
        message=kabadi.objects.all()

    
    context = {
        'message': message,
    }
    return render(request, 'results.html', context)
