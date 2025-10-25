from django.shortcuts import render
from events.models import Event

# Create your views here.

def event_list(request):
    event = Event.objects.all()
    response = {'data' : event}
    return render(request, 'model-agenda.html', response)