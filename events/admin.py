from django.contrib import admin
from events.models import Event

# Register your models here.

class AdminEvent(admin.ModelAdmin):
    list_display = ('title', 'description', 'event_date', 'created_at', 'user')
    list_filter = ('title', 'event_date', 'created_at')

admin.site.register(Event, AdminEvent)