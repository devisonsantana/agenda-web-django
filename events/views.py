from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest
from events.models import Event

# Create your views here.

@login_required(login_url='/login/')
def event_list(request:HttpRequest):
    event = Event.objects.filter(user=request.user)
    response = {'data' : event}
    return render(request, 'model-agenda.html', response)

def login_user(request:HttpRequest):
    return render(request, 'login.html')

def submit_user(request:HttpRequest):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Provided user or password invalid')
    return redirect('/')

def  logout_user(request):
    logout(request)
    return redirect('/')