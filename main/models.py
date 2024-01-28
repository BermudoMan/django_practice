from django.db import models

class GalleryItem(models.Model):
    file = models.FileField(upload_to='main/static/main/img')

    title = models.CharField('title', max_length=150)
    text = models.TextField('some_info')

    def __str__(self):
        return self.title


class Events(models.Model):
    text = models.TextField('Event')
    date = models.DateField('Pub. date')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


