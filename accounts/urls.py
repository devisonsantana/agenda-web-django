from django.urls import path
from . import views

urlpatterns = [
    path(route='login/', view=views.login_user, name='login'),
    path(route='register/', view=views.create_user, name='register'),
    path(route='profile/', view=views.profile_user, name='profile'),
    path(route='profile/edit', view=views.edit_profile, name='edit_profile'),
    path(route='logout/', view=views.logout_user, name='logout'),
]