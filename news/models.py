from django.db import models


class Events(models.Model):
    text = models.TextField('Event')
    date = models.DateField('Pub. date')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

