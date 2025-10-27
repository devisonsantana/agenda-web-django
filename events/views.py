from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest
from events.models import Event

# Create your views here.

def index(request):
    return render(request, 'index.html')

# TODO: create new user

# TODO: create new event
# TODO: update a event
# TODO: delete a event

@login_required(login_url='/login')
def event_list(request):
    event = Event.objects.filter(user=request.user)
    response = {'data' : event}
    return render(request, 'agenda.html', response)

def login_user(request):
    return render(request, 'login.html')

def submit_user(request:HttpRequest):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/agenda')
        else:
            messages.error(request, 'Provided user or password invalid')
    return redirect('/login')

def  logout_user(request):
    logout(request)
    return redirect('/')