from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from events.models import Event
from django.contrib import messages

@login_required(login_url='/login')
def get_all_events(request: HttpRequest):
    events = Event.objects.filter(user=request.user).order_by('-event_date')
    context = {
        'events': events
    }
    return render(request=request, template_name='agenda.html', context=context)

@login_required(login_url='/login')
def add_event(request: HttpRequest):
    if request.POST:
        title = request.POST.get('title').strip()
        event_date = request.POST.get('event-date')
        description = request.POST.get('description').strip()
        user = request.user

        if not title:
            messages.error(request=request, message='O título é obrigatório.')
            return redirect(to='new')
        
        if not event_date:
            messages.error(request=request, message='A data é obrigatória.')
            return redirect(to='new')
        
        Event.objects.create(title=title, event_date=event_date, description=description, user=user)
        
        return redirect(to='agenda')
    return render(request=request, template_name='event.html')

@login_required(login_url='/login')
def edit_event(request: HttpRequest):
    event_id = request.GET.get('id')
    
    if request.method == 'POST':
        event = get_object_or_404(klass=Event, id=event_id, user=request.user)
        title = request.POST.get('title').strip()
        event_date = request.POST.get('event-date')
        description = request.POST.get('description').strip()
        
        if not title:
            messages.error(request=request, message='O titulo é obrigatório.')
            return redirect(to=f'/agenda/edit?id={event_id}')
        
        if not event_date:
            messages.error(request=request, message='A data é obrigatória.')
            return redirect(to=f'/agenda/edit?id={event_id}')
        
        event.title = title
        event.event_date = event_date
        event.description = description
        event.save()
        return redirect(to='agenda')
    
    if event_id:
        event = get_object_or_404(klass=Event, id=event_id, user=request.user)
        context = {
            'event': event
        }
        return render(request=request, template_name='event.html', context=context)
    return redirect(to='agenda')

@login_required(login_url='/login')
def delete_event(request: HttpRequest, id: int):
    event = get_object_or_404(Event, id=id, user=request.user)
    event.delete()
    return redirect('agenda')