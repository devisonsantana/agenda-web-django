from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.get_all_events, name='agenda'),
    path(route='new/', view=views.add_event, name='new'),
    path(route='edit', view=views.edit_event, name='edit'),
    path(route='delete/<int:id>', view=views.delete_event, name='delete')
]

"""
    path('agenda/', views.event_list, name='agenda'),
    path('agenda/new/', views.event_create, name='new'),
    path('agenda/new/submit', views.submit_event),
    path('agenda/edit', views.event_update, name='edit'),
    path('agenda/edit/submit', views.submit_event),
    path('agenda/delete/<int:id>', views.event_delete, name='delete'),
"""