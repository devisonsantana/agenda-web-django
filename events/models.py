from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField(verbose_name='Event Date')
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_event_date(self):
        return self.event_date.strftime('%d/%m/%Y %H:%M')

    def get_event_date_input(self):
        return self.event_date.strftime('%Y-%m-%dT%H:%M')
    
    class Meta:
        db_table = 'event'