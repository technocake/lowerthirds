# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib.parse

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView

from .models import LowerThird, Event
from . import services


class EventListView(ListView):
    model = Event


def lowerthird(request, id):
    '''
        The birthday lowerthird
    '''
    item = get_object_or_404(LowerThird, pk=id)
    template = item.template.file_name

    data = {
        'name': item.name,
        'title': item.title,
    }
    return render(request, template, data, content_type='image/svg+xml')  # noqa


def lowerthirds(request):
    lowerthirds = get_list_or_404(LowerThird)
    return render(request, 'lowerthirds.html', {'lowerthirds': lowerthirds})


def event(request, id):
    '''
        The streaming event
    '''
    event = get_object_or_404(Event, pk=id)
    data = {
        'event': event,
    }
    return render(request, 'event.html', data)  # noqa


def event_download(request, id):
    '''
        The birthday event
    '''
    event = get_object_or_404(Event, pk=id)

    zipfile = services.export_graphics(event)
    zipdata = services.zipfile_to_bytes(zipfile)

    friendly_name = urllib.parse.quote('{}.zip'.format(event.name.replace(' ', '_')))

    response = HttpResponse(content_type="application/zip")
    response["Content-Disposition"] = "attachment; filename={}".format(friendly_name)  # noqa
    response.write(zipdata)
    return response


def events(request):
    '''
        List all events
    '''
    events = get_list_or_404(Event)
    return HttpResponse('Ikke noe her enda.')
    return render(request, 'events.html', {'events': events})
