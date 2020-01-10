# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse

from .models import LowerThird, Event, Template


class LowerThirdAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'event')
    search_fields = (
        'name',
        'title',
        'event__name',
        'event__location',
        'event__start',
        'event__end'
    )
    sortable = ('name', 'title', 'event')

    def view_on_site(self, obj):
        url = reverse('lowerthird', args=(obj.id,))
        return url


class LowerThirdInline(admin.TabularInline):
    '''
    Makes it possible to create lower thirds
    directly on a event page from admin.
    '''
    model = LowerThird


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'start',
        'end'
    )
    search_fields = (
        'name',
        'location',
        'start',
        'end'
    )
    sortable = (
        'name',
        'location',
        'start',
        'end'
    )

    inlines = (
        LowerThirdInline,
    )

    def view_on_site(self, obj):
        url = reverse('event', args=(obj.id,))
        return url


admin.site.register(LowerThird, LowerThirdAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Template)

