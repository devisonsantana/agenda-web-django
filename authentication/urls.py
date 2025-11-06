from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name='home'),
    path(route='login/', view=views.login_user, name='login'),
    path(route='logout/', view=views.logout_user, name='logout'),
]