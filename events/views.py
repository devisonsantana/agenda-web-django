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

@login_required(login_url='/login')
def event_create(request):
    return render(request, 'create-event.html')

@login_required(login_url='/login')
def submit_event(request:HttpRequest):
    if request.POST:
        id = request.POST.get('id')
        title = request.POST.get('title')
        event_date = request.POST.get('event-date')
        description = request.POST.get('description')
        user = request.user
        if id:
            Event.objects.filter(id=id, user=user).update(title=title, description=description, event_date=event_date)
        else:
            Event.objects.create(title=title, description=description, event_date=event_date, user=user)
    return redirect('/agenda')

# TODO: update a event

@login_required(login_url='/login')
def event_update(request:HttpRequest):
    id = request.GET.get('id')
    if id:
        user = request.user
        data = {}
        data['event'] = Event.objects.filter(user=user).get(id=id)
    return render(request, 'edit-event.html', data)

# TODO: delete a event

@login_required(login_url='/login')
def event_delete(request:HttpRequest, id):
    event = Event.objects.get(id=id)
    if event.user == request.user:
        event.delete()
    return redirect('/agenda')


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

def logout_user(request):
    logout(request)
    return redirect('/')