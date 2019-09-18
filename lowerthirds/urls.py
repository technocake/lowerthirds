"""lowerthirds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from graphics import views as graphics


admin.site.site_header = 'Creative Crew Bergen - lowerthirds generator'

admin.autodiscover()

urlpatterns = [
    path('', graphics.index),
    path('admin/', admin.site.urls),
    path('lowerthird/<int:id>', graphics.lowerthird, name='lowerthird'),
    path('lowerthirds', graphics.lowerthirds, name='lowerthirds'),

    path('event/<int:id>', graphics.event, name='event'),
    path('event/<int:id>/download', graphics.event_download, name='event_download'),
    path('events', graphics.events, name='events'),
]
