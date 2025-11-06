from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from events.models import Event

# TODO: create new user

@login_required(login_url='/login')
def add_event(request):
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
    return render(request, 'create-event.html')

# TODO: update a event

@login_required(login_url='/login')
def edit_event(request:HttpRequest):
    id = request.GET.get('id')
    if id:
        user = request.user
        data = {}
        data['event'] = Event.objects.filter(user=user).get(id=id)
        return render(request, 'edit-event.html', data)
    return redirect('/agenda')

# TODO: delete a event

@login_required(login_url='/login')
def delete_event(request:HttpRequest, id):
    event = Event.objects.get(id=id)
    if event.user == request.user:
        event.delete()
    return redirect('/agenda')


@login_required(login_url='/login')
def get_all_events(request):
    event = Event.objects.filter(user=request.user)
    response = {'data' : event}
    return render(request, 'agenda.html', response)
