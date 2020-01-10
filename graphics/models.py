# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Template(models.Model):
    file_name = models.CharField(max_length=255, help_text="filnavn på template for grafikk.")  # noqa

    def __str__(self):
        return self.file_name


class LowerThird(models.Model):
    name = models.CharField(max_length=255, help_text='Navnet til den som er på tv.')  # noqa
    _title = models.CharField(max_length=255, help_text='Tittelen på talken', blank=True, null=True)  # noqa

    template = models.ForeignKey('Template', related_name='template', on_delete=models.CASCADE, blank=True, null=True)  # noqa
    event = models.ForeignKey('Event', related_name='lowerthirds', on_delete=models.CASCADE)  # noqa

    @property
    def title(self):
        """
            Showing None as blank string
        """
        if self._title is None:
            return ""
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def __str__(self):
        return '{} - {}'.format(self.name, self.title)


class Event(models.Model):
    name = models.CharField(max_length=255, help_text='Navnet på stream eventet.')  # noqa
    notes = models.TextField(help_text='Optional notes for the event.', blank=True, null=True)  # noqa
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
