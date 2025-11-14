from django.utils import timezone
from django.conf import settings
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField(verbose_name='Event Date')
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_event_date(self):
        local_date = timezone.localtime(self.event_date)
        return local_date.strftime('%d/%m/%Y %H:%M')

    def get_event_date_input(self):
        local_date = timezone.localtime(self.event_date)
        return local_date.strftime('%Y-%m-%dT%H:%M')
    
    class Meta:
        db_table = 'event'