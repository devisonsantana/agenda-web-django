"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.event_list, name='agenda'),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_user, name='submit'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.index, name='home'),
]
