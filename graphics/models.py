# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class LowerThird(models.Model):
    name = models.CharField(max_length=255, help_text='Navnet til den som er på tv.')  # noqa
    title = models.CharField(max_length=255, help_text='Tittelen på talken')  # noqa

    event = models.ForeignKey('Event', related_name='lowerthirds', on_delete=models.CASCADE)  # noqa

    def __str__(self):
        return '{} - {}'.format(self.name, self.title)


class Event(models.Model):
    name = models.CharField(max_length=255, help_text='Navnet på stream eventet.')  # noqa
    location = models.CharField(max_length=255, help_text='Stedet det streames ifra.', blank=True, null=True)  # noqa
    start = models.DateTimeField(help_text='Når arrangmentet starter', blank=True, null=True)  # noqa
    end = models.DateTimeField(help_text='Når arrangmentet stopper', blank=True, null=True)  # noqa

    def __str__(self):
        if self.start:

            if self.end:
                return '{} ({} - {})'.format(self.name, self.start, self.end)  # noqa

            return '{} ({})'.format(self.name, self.start)  # noqa
        else:
            return '{}'.format(self.name)
